// Game.js
var SideScroller = SideScroller || {};
SideScroller.Game = function(){};
SideScroller.Game.prototype = {
	preload: function(){
		this.game.time.advancedTiming = true;
	},

	create: function(){
		this.map = this.game.add.tilemap('level1');

		// the first parameter is the tileset name as specified in Tiled, the second is the key to the asset
		this.map.addTilesetImage('ssterrain','ssterrain');

		// create layers
		// this.skyLayer = this.map.createLayer('skyLayer');
		this.backgroundLayer0 = this.map.createLayer('backgroundLayer0');
		this.backgroundLayer1 = this.map.createLayer('backgroundLayer1');
		this.blockedLayer = this.map.createLayer('blockedLayer');

		// fix delta scrolling
		this.backgroundLayer1.renderSettings.enableScrollDelta = false;

		// collision on blockedLayer
		this.map.setCollisionBetween(1,100000,true,'blockedLayer');


		// resizes the game world to match the layer dimensions
		this.backgroundLayer0.resizeWorld();

		// create player
		this.player = this.game.add.sprite(64,384,'morty');
		this.player.frame = 0;

		// create player animation
		this.player.animations.add('left',[4,3], 10, true);
		this.player.animations.add('right',[2,1], 10, true);

		// enable physics on the player
		this.game.physics.arcade.enable(this.player);

		// player gravity
		this.player.body.gravity.y = 1500;

		//the camera will follow the player in the world
		this.game.camera.follow(this.player);

		// initial cursor keys
		this.cursors = this.game.input.keyboard.createCursorKeys();
	},

	update: function(){
		// collision detection
		this.game.physics.arcade.TILE_BIAS = 40;
		this.game.physics.arcade.collide(
			this.player,
			this.blockedLayer
			);

		// reset the players velocity (movement)
		this.player.body.velocity.x = 0;

		if(this.cursors.left.isDown){
			// move to the left
			this.player.body.velocity.x -= 200;
			this.player.animations.play('left');
		}
		else if(this.cursors.right.isDown){
			// move to the right
			this.player.body.velocity.x += 200;
			this.player.animations.play('right');
		}
		else{
			// stand still
			this.player.animations.stop();
			if(this.player.frame == 0 || this.player.frame == 1 || this.player.frame == 2){
				this.player.frame = 0;
			} else if(this.player.frame == 3 || this.player.frame == 4 || this.player.frame == 5) {
				this.player.frame = 5;
			}
		}

		// keybindings
		if(this.cursors.up.isDown && this.player.body.blocked.down){
			this.player.body.velocity.y = -549;
		}
	},

	playerHit: function(player, blockedLayer){

	},

	render: function(){
		this.game.debug.text(this.game.time.fps || '--',16,32,"#3f3f3f","16px Consolas");
	}
};