import sys
import re

def Red(mess)-> str:
    """
    function that colors red text
    :param mess:str
    :return:str Red text
    """
    return "\033[91m {}\033[01m" .format(mess)

def Green(mess) ->str:
    """
      function that colors green text
      :param mess:str
      :return:str green text
      """
    return "\033[32m {}\033[01m" .format(mess)

def password_validator (passW:str):
    """
    function Verifies passwords :

    length of at least 10 characters.

    least one lowercase letter between a-z

    least one capital letter between A-Z.

    :param passW: str: Password
    :return:None
    """
    error_mess = "Password error not verified You must enter at:\n"
    bo = False
    if len(passW).__lt__(10):
        bo=True
        error_mess += " length of at least 10 characters.\n"
    if not re.match("(?=.+[\d])",passW):
        bo=True
        error_mess += " least one digit between 0-9.\n"
    if not re.match("(?=.+[a-z])",passW):
        bo=True
        error_mess += " least one lowercase letter between a-z.\n"
    if not re.match("(?=.+[A-Z])",passW):
        bo=True
        error_mess += " least one capital letter between A-Z.\n"
    if bo:
        sys.exit(Red(error_mess))
    else:
        sys.stdout.writelines(Green("Password verified!!."))
        sys.exit()

def Read_file(path:str)->str:
    """
    function File reading
    :param path: str: path of a file
    :return: str: Text in file
    """
    with open(path, "r") as file:
      return file.readline()


if __name__ == '__main__':

    if len(sys.argv) <= 3 and len(sys.argv)>1:
        if sys.argv[1] == "-f":
            password_validator(Read_file(sys.argv[2]))
        else:
            password_validator(sys.argv[1])
    else:
        sys.exit(Red("Error You must submit one or two arguments"
                     "\n 1 argument to a password"
                     "\n 2 arguments [-f] and path of a file .txt"))
