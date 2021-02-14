import zombiedice

class MyZombie:
    def __init__(self, name):
        self.name = name

    def count_colors(self, results):

        color_count = {}

        for color, icon in results['rolls']:
            color_count.setdefault(color, 0)
            color_count[color] += 1
            
        return color_count

    def turn(self, gameState):
        #colors = self.count_colors(results)
        shotguns = 0

        while shotguns < 2:
            results = zombiedice.roll()

            if results is None:
                return

            shotguns += results['shotgun']

        else:
            return

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='Austin Bot')
)

zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)