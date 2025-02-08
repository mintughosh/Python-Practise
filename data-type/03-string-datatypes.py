
sentence = "this is Python world"
text = "   Some spaces around   "

## String Split
print(sentence.split())

## String lenghth
print("Length of the sentence: ", len(sentence))

## Strip Text
print("Stripped text: ", text.strip())

### Concat String
print("Concatenation of Sentences and text would look like: ", sentence + " with" + text)

### Replace String
print("Modified text: ", sentence.replace('world', 'universe'))