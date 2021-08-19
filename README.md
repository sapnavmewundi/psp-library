Requirements:

I. Ubuntu Basic Node Setup
1. Install Redis
2. Install MySQL
3. Python 3.6
4. pip install -r requirements.txt
5. Edit setenv.sh file with enviornments
6. Celery configuration


II. Download and Validate PDB files from CSV file
input file: allproteins_p1.csv
-- Download PDB files
Download_async_pdb.py
-- Validate PDB files
validate_pdb.py


III. DataBase Preparation

--creating tables
python db.py create

--deleting tables
python db.py destroy


IV. Data Preparation
a. Running Process

1. python processor.py --> Breaks 100 PDBs into DB and Redis by calling tasks.py
	Function is defined to process PDB
        	process_pdb --> gets all PDB detils to process further
	Function is defined to break the PDB files
		Process_break --> breaks PDB files into fragments of size 3 to 41 and puts in tables created 

2. python finalsuperimposerdb.py --> performs superimposition to generate RMSD values by calling tasks.py
	Function is defined to identify identical fragmets from tables
		process_batch --> uses util.get-table-name, for each table name find the identical combinations,lists them and also gives number of combinations found
	function is defined to perform superimposition 
		process_comb --> superimposition of identicalfragments is performed using SVD superimposer to generate RMSD values and puts results in all_combination table in database using util.insert_all_combinations

3. python minrms.py -->takes aii_combinations as input and generates table of minrmsdcobination which has min RMSD value for every combinations found(froom fragment size 3 to 4a, all in one)

4. Based on statistical analysis, Skewness and Kurtiosis values the fragment are grouped into variant and in variant ones.


IV. Query phase

python. testseq6.py

1. Brak the query into fragment size 3 to 41
2. Recursively find the matching sequence based on residue in invariant fragment library( 10 times) --> implemented using Brute Force method
3. Creation of PDB structure 


Output: Output folder with PDB files
