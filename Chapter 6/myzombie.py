import zombiedice

class MyZombie:
    def __init__(self, name):
        self.name = name

    def count_colors(self, results):

        if results is None:
            return

        color_count = {}

        for color, icon in results['rolls']:
            color_count.setdefault(color, 0)
            color_count[color] += 1
            
        return color_count

    def turn(self, gameState):
        #colors = self.count_colors(results)
        shotguns = 0
        turn_count = 0

        while shotguns < 2:
            results = zombiedice.roll()
            turn_count += 1
            colors  = self.count_colors(results)

            if results is None:
                return

            shotguns += results['shotgun']

        if colors.get('red', 0) == 3 and turn_count < 5:  # try an extra roll if no red die in cup
            results = zombiedice.roll()
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