## SoundManager

**SoundManager** is a Borg-style object that controls sound effects and music playback. Initialize it once using `SoundManager().init_sound_manager()`, then get a handle to it later on by simply creating a `SoundManager()` object.

To load sound effects, call `[soundmanager].load_sound()`, passing in the name of the clip and an optional format (defaults to 'ogg'). **SoundManager** looks for files in `res/audio/`. For example, to load "beep.wav" from the audio resource folder call `[soundmanager].load_sound("beep","wav")`. To play this sound effect after loading, just call `[soundmanager].play("beep")`.

Music is handled similarly, with the `load_music()` and `start_music(index)` methods. Music is referenced by index, rather than by track name -- to get the index for a track by name use `get_track_number(name)`. You can enable or disable music shuffling via `[soundmanager].shuffle(boolean)`.

##### A complete example:

<code>
	# Somewhere early on:
	SoundManager().init_sound_manager()
	
	# As you load a level:
	sound = SoundManager()
	sound.load_sound("victory","wav")
	sound.load_music("background")
	sound.start_music(sound.get_track_number("background"))
	
	# Play 'victory' jingle:
	sound.play("victory")
</code>