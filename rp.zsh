# Open a fzf selection of uniquelly tagged intervals
# from a time period given on the command line if not period is given
# default to 1 year

# Put the selected interval on the prompt for further manipulation

# zsh only,
# this must be sourced from  .zshrc
# source ~/path/rp.zsh


rp() {
 # Stop any running interval
 timew stop

 OUTPUT=$(timew twfzf ${1:-1y} rc.printonly=true)
 print -z $OUTPUT
}

