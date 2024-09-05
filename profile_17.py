from g2glisterbot2 import G2GListerBot
import datetime

if __name__ == "__main__":
    bot = G2GListerBot("Profile 17")
    file = open(r'C:\Users\BABAR\Desktop\g2g_all_games_listing_bot_modified\log_17.txt','a')
    file.write(f'{datetime.datetime.now()} - the script start running \n')
    
    bot.run()

    file = open(r'C:\Users\BABAR\Desktop\g2g_all_games_listing_bot_modified\log_17.txt','a')
    file.write(f'{datetime.datetime.now()} - the script has successfully ran \n')

