from direct.showbase.ShowBase import ShowBase
class Game(ShowBase):
  def __init__(self):
      ShowBase.__init__(self)
      self.model = loader.loadModel('models/environment')
      self.model.reparentTo(render)
game = Game()
game.run()
