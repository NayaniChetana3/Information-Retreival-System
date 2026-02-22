There are six information retrival files
LSA,Hybrid(VSM),Glasgow_LSA,LDA,Baseline,BM25

To test your code, run main.py as before with the appropriate arguments.
Usage: main.py [-custom] [-dataset DATASET FOLDER] [-out_folder OUTPUT FOLDER]
               [-segmenter SEGMENTER TYPE (naive|punkt)] [-tokenizer TOKENIZER TYPE (naive|ptb)] 
               [-method (lsa|vsm|glsa|lda|baseline|bm25)] 
               [-ngram (uni|bi|hyb)]
               [-k (value between 50-1400)]

Plots are produced in final_plots folder with relevant file name. 
Default settings are lsa method with hybrid model and 250 concepts.

Some sample plots and their corresponding evaluations are present in final_plots and final_outputs folder respectively.

pip install rank_bm25 to use bm25 algorithm

When the -custom flag is passed, the system will take a query from the user as input. For example:
> python main.py -custom
> Enter query below
> Papers on Aerodynamics

This will print the IDs of the five most relevant documents to the query to standard output.

When the flag is not passed, 
all the queries in the Cranfield dataset are considered and 
precision@k, recall@k, f-score@k, nDCG@k and the Mean Average Precision are computed.

