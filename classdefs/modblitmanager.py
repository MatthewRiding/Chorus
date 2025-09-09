class BlitManager:
    def __init__(self, canvas, animated_artists=()):
        """
        Parameters
        ----------
        canvas : FigureCanvasAgg
            The canvas to work with, this only works for subclasses of the Agg
            canvas which have the `~FigureCanvasAgg.copy_from_bbox` and
            `~FigureCanvasAgg.restore_region` methods.

        animated_artists : Iterable[Artist] List of the artists set as 'animated' that will need to be managed.
        These artists will not be drawn by the standard canvas draw_event (due to their 'animated=True' status),
        so the BlitManager needs to do this work.  All other artists will form the 'background'.
        """
        self.canvas = canvas
        self._bg = None
        self._animated_artists = []

        for a in animated_artists:
            self.add_artist(a)

        # Grab the background and draw the animated artists on every draw_event:
        self.cid = canvas.mpl_connect("draw_event", self.on_draw_event)

    def on_draw_event(self, event):
        """Callback to register with Matplotlib 'draw_event'."""
        if event is not None:
            if event.canvas != self.canvas:
                raise RuntimeError
        # Matplotlib has drawn all the non-animated artists already.  Save the current figure image as the
        # 'background' (_bg):
        self._bg = self.canvas.copy_from_bbox(self.canvas.figure.bbox)
        # Having saved an image of the background, we can now proceed to draw all the 'animated=True' artists not
        # drawn by Matplotlib automatically:
        self._draw_all_animated()

    def add_artist(self, artist):
        """
        Add an artist to be managed.

        Parameters
        ----------
        artist : Artist

            The artist to be added.  Will be set to 'animated' (just
            to be safe).  *artist* must be in the figure associated with
            the canvas this class is managing.

        """
        if artist.figure != self.canvas.figure:
            raise RuntimeError
        artist.set_animated(True)
        self._animated_artists.append(artist)

    def _draw_all_animated(self):
        """Draw all of the animated artists under management."""
        for artist in self._animated_artists:
            self.canvas.figure.draw_artist(artist)

    def blit_all_animated_artists(self):
        """Update the screen with all animated artists using blitting."""
        # In case there is no saved background:
        if self._bg is None:
            self.on_draw_event(None)
        else:
            # Restore the background from the saved image:
            self.canvas.restore_region(self._bg)
            # Draw all the animated artists using the cached renderer:
            self._draw_all_animated()
            # Blit the result to the screen: (This pushes the updated RGBA buffer from the
            # renderer to the GUI framework so that you can see it)
            self.canvas.blit(self.canvas.figure.bbox)
        # Let the GUI event loop process anything it has to do:
        #self.canvas.flush_events()

    def delete_last_artist(self):
        del self._animated_artists[-1]
