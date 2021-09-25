from listener import EmailListener, PhoneListener
from editor import check_for_new_episode, check_for_new_movie


# Initialize event listeners
EmailListener()
PhoneListener()

# check for new episode
check_for_new_episode('See', 'see.s01e01')

# check for new movie
check_for_new_movie('The Green Knight')





