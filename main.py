import socket
import re



# site_arr= ['berezka.ae', 'dan-okna.ru', 'danokna.ru', 'danokna24.ru', 'dubnadent.ru', 'felix69.ru', 'foodiclub.site', 'glavstroyremont.ru', 'kaspack.ru', 'klimatprolife.ru', 'oknokaleva.ru', 'orientalelectro.ru', 'sk-polimer.ru', 'test-owmedia.ru', 'thai-day.ru', 'veka.danokna.ru', 'vladlena-beauty.ru', 'wh.danokna.ru']
#

def read_txt():
    with open('domain_names.txt', 'r') as f:
        # Read the file line by line
        lines = f.readlines()

    # Iterate over the lines
    for line in lines:
        # Strip the line of whitespace characters
        line = line.strip()
        # Add the domain to the list
        site_arr.append(line)

    # Print the list

    return site_arr



def check_ip():

    for i in site_arr:

        try:
            ip = socket.gethostbyname(i)
            if ip == "31.31.198.196":
                print(f'https://www.{i} {ip} good')
                # pass
            else:
                print(f'{i} {ip}  bad')
                # pass
        except:
            print (f'{i}: не доступен')
            # pass
def main():
    global site_arr
    site_arr = []
    read_txt()
    check_ip()




if __name__ == '__main__':
    main()