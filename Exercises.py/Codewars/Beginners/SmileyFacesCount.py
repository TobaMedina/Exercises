# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.
# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

def count_smileys(arr):
    count = 0
    for face in arr:
        if len(face) == 2:
            if face[0] in [':', ';'] and face[1] in [')', 'D']:
                count += 1
        elif len(face) == 3:
            if face[0] in [':', ';'] and face[1] in ['-', '~'] and face[2] in [')', 'D']:
                count += 1
    return count


print(count_smileys([':)', ';(', ';}', ':-D', ';D']))
