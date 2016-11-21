// Preload.js
var SideScroller = SideScroller || {};

// loading the game assets
SideScroller.Preload = function(){};
SideScroller.Preload.prototype = {
	preload: function(){
		// show loading screen
		this.preloadBar = this.add.sprite(
			this.game.world.centerX,
			this.game.world.centerY,
			'preloadbar'
			);
		this.preloadBar.anchor.setTo(0.5);
		this.preloadBar.scale.setTo(3);
		this.load.setPreloadSprite(this.preloadBar);

		// load game assets
		this.load.tilemap(
			'level1', // name?
			'/static/tilemaps/level1.json', // filepath
			null, // not sure
			Phaser.Tilemap.TILED_JSON
			);
		this.load.image('ssterrain','/static/img/ss.terrain.png');
		this.load.spritesheet('morty','/static/img/ss.morty.png',32,64);
		this.load.audio('coin','/static/audio/coin.wav');
	},

	create: function(){
		this.state.start('Game');
	}
};