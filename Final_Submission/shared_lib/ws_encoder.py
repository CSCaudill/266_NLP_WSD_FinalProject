
import collections

class WS_Encoder(object):
    
  """SIGNIFICANTLY LEVERAGED VOCABULARY.PY FROM ASSIGNMENT 3"""

#   START_TOKEN = "<s>"
#   END_TOKEN = "</s>"
  UNK_TOKEN = "<unk>"

  def __init__(self, tokens, size=None):
    self.unigram_counts = collections.Counter(tokens)
    # leave space for "<s>", "</s>", and "<unk>" - MODIFYING
    #leave space now just for "<unk>"
    
    top_counts = self.unigram_counts.most_common(None if size is None else (size - 1))
    ws_vocab = ([self.UNK_TOKEN] +
             [w for w,c in top_counts])
    
    ### NOTE: is actually ID to WORD SENSE, but left as ID TO WORD to allow for easier naming between files
    
    # Assign an id to each word, by frequency
    self.id_to_word_sense = dict(enumerate(ws_vocab))
    self.word_sense_to_id = {v:k for k,v in self.id_to_word_sense.iteritems()}
    self.size = len(self.id_to_word_sense)
    if size is not None:
        assert(self.size <= size)

    # For convenience
    self.wordset = set(self.word_sense_to_id.iterkeys())

    # Store special IDs
#     self.START_ID = self.word_to_id[self.START_TOKEN]
#     self.END_ID = self.word_to_id[self.END_TOKEN]
    self.UNK_ID = self.word_sense_to_id[self.UNK_TOKEN]

  def word_senses_to_ids(self, words):
    return [self.word_sense_to_id.get(w, self.UNK_ID) for w in words]

  def ids_to_word_senses(self, ids):
    return [self.id_to_word_senses[i] for i in ids]

#   def sentence_to_ids(self, words):
#     return [self.START_ID] + self.words_to_ids(words) + [self.END_ID]

  def ordered_word_senses(self):
    """Return a list of words, ordered by id."""
    return self.ids_to_word_senses(range(self.size))