// Boot.js
var SideScroller = SideScroller || {};
SideScroller.Boot = function(){};

// setting game configuration and loading the assets for the loading screen
SideScroller.Boot.prototype = {
	preload: function(){
		// assets we'll use in the loading screen
		this.load.image('preloadbar','/static/img/preloader-bar.png');
	},
	create: function(){
		// loading screen will have a blue background
		this.game.stage.backgroundColor = '#B3E5FC';

		// scaling options
		this.scale.scaleMode = Phaser.ScaleManager.SHOW_ALL;

		// have the game centered horizontally
		this.scale.pageAlignHorizontally = true;
		this.scale.pageAlignVertically = true;

		// screen size will be set automagically
		// this.scale.setScreenSize(true);

		// physics system
		this.game.physics.startSystem(Phaser.Physics.ARCADE);

		this.state.start('Preload');
	}
};