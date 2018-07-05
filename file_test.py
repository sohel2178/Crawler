
# f= open('test.txt','r')

# print(f.mode)

# f.close()

# Context Manager

# with open('test.txt','r') as f:
    # Read all the Content
    # f_content = f.read()

    # There is another method to read a file line by line

    # f_content = f.readlines()
    # print(f_content)

    # Another way to read All of the Lines. Better Method then Above

    # for line in f:
    #     print(line,end='')

    # More Control Method to Read File

    # if we pass 100 as an argument then it read 100 character from the file


    # f_content = f.read(20)
    # print(f_content,end='')

    # f_content = f.read(20)
    # print(f_content,end='')

    # f_content = f.read(20)
    # print(f_content,end='')

    # size_to_read = 20
    # f_content = f.read(size_to_read)

    # If we reached the end of the file length of the f_content will be zero
    # while len(f_content)>0:
    #     print(f_content,end='***')
    #     # print(f.tell())
    #     # print(f.seek())
    #     f_content = f.read(size_to_read)


    # !!!! Wrinting a File !!!

# with open('test2.txt','w') as f:
#     f.write('Hey Sohel How Are You')
#     f.seek(0)

#     f.write('Hey Sohel How Are You')
#     f.seek(0)

#     f.write('Hey Sohel How Are You')
#     f.seek(0)


# !!! Copying Content of a File !!!

# with open('test.txt','r') as fr:

#     with open('test_copy.txt','w') as fw:
#         for line in fr:
#             fw.write(line)


# !!! Copying Image File !!!

# with open('mobi.png','rb') as fr:

#     with open('mobi_copy.png','wb') as fw:
#         for line in fr:
#             print(line)


# !!! Print Binary File and Examine !!!
# with open('mobi.png','rb') as fr:
#     print(fr.read())


# !!! Read and Write Chunk by Chunk !!!
with open('mobi.png','rb') as fr:
    chunk_size = 4096

    with open('mobi_copy.png','wb') as fw:
        chunk_data = fr.read(chunk_size)

        while len(chunk_data) > 0:
            fw.write(chunk_data)
            chunk_data = fr.read(chunk_size)

