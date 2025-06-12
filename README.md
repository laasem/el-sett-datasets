# El Sett Datasets
Training, validation, and test datasets for [El Sett](https://colab.research.google.com/drive/1wdeh6w5Tm1CTFD-kJ1xMA4iO6qkpcf_Y?usp=sharing), a fine-tuned GPT-2 model that generates Umm Kulthumm song endings.

## Dataset generation methodology
A corpus of 89 Umm Kulthum song lyrics was generated from a Scribd document curated by user Ahmed Amer (Amer, 2013). To create the dataset, the Scribd document was first converted to a plain text file to remove formatting, and then programmatically trimmed, divided into songs, and partitioned into training (81 songs), validation (4 songs), and test (4 songs) data. Each partition was written to a separate CSV file, all following the same format: a “target_text” column containing the last 4 lines and an “input_text” column containing the song lyrics minus the ones in the “target_text” column.

## References
Amer, A. (2013, January 30). أغانى أم كلثوم مكتوبة [Aghani Umm Kulthum Maktubah] [Document]. Scribd. https://www.scribd.com/doc/123012647/%D8%A3%D8%BA%D8%A7%D9%86%D9%89-%D8%A3%D9%85-%D9%83%D9%84%D8%AB%D9%88%D9%85-%D9%85%D9%83%D8%AA%D9%88%D8%A8%D8%A9-doc

Aubmindlab. (n.d.). *Preprocess.py*. GitHub. https://github.com/aub-mind/arabert/blob/master/preprocess.py


_Developed as part of the Computational Semantics course of the Universitat Pompeu Fabra's Master in Theoretical and Applied Linguistics taught by Gemma Boleda, Marta Garcia Casado, and Matéo Mahaut, from which some code was adapted._


