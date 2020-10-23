##simple guessing game using one word.
secret_word='kayden'
guess=''
guess_count=0
guess_limit=3
out_of_guesses= False

print ("Try to guess my favorite star")

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess=input("Enter word to guess:")
        guess_count+=1
    else:
        out_of_guesses=True

if out_of_guesses:
    print("You have only 3 guesses! Sorry - YOU LOSE!")
else:
    print("Your guess is Right! " + guess + " is right answer!!!")