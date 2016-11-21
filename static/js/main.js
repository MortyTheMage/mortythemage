// Main.js
var SideScroller = SideScroller || {};
SideScroller.game = new Phaser.Game(1280, 768, Phaser.CANVAS, '');
SideScroller.game.state.add('Boot', SideScroller.Boot);
SideScroller.game.state.add('Preload', SideScroller.Preload);
SideScroller.game.state.add('Game', SideScroller.Game);
SideScroller.game.state.start('Boot');