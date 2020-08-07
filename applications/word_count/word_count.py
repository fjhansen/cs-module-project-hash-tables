def word_count(s):
    # Your code here
    cache = {}
    words = s.split()

    if s == "":
        print(s,"dasd")
        return {}

    for w in words:
        print(w)
        w = w.lower()
        q_word = ""
        print("QWORD_1: ",q_word)
        for l in w:
            if l.isalnum() or l == "\'":
                q_word += l
                print("QWORD_2: ",q_word)
        if q_word in cache:
            cache[q_word] += 1
            #print("TESTING1: ",cache)
        elif q_word == "":
            return {}
        else:
            cache[q_word] = 1
            print("CATCHE: \n",cache)
    c_words = dict(cache.items())
    return c_words
                
        

    



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

#   " : ; , . - + = / \ | [ ] { } ( ) * ^ &

