# Jordan Allen
# ZyLab 10.15

class Team:
    def __init__(self):
        self.team_wins = None
        self.team_name = None
        self.team_losses = None

    def init(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        win_percentage = self.team_wins / (self.team_wins + self.team_losses)
        return win_percentage


if __name__ == '__main__':
    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

    if team.get_win_percentage() < 0.5:
        print('Team', team.team_name, 'has a losing average.')
    else:
        print('Congratulations, Team', team.team_name, 'has a winning average!')
