# GEM-example
This repository provides the code and example data of the paper "Gradient Boosting-accelerated Evolution for Multiple-Fault Diagnosis"

## Usage

1. To run the first stage of **GEM** , you need to go to the work folder, with circuit.bench、circuit.faults、circuit.test and the corresponding fault simulation results. Then simply execute

```
./GEM-stage1 circuit begin end
```

where begin and end are used to limit the range of fault simulation results. Subsequently, the folder train_and_test was generated, which contains the csv files extracted from the fail log for training the HGB model.

2. To train HGB model and make prediction, execute

```
python training.py
python predicting.py
```

3. To run the second stage of **GEM**, execute

```
./GEM-stage2 circuit begin end
```

where begin and end are used to limit the range of fault simulation results. The folder x_ans is then generated, where the .out file is the final diagnostic result.

## Environment

· gcc 11.4.0 Ubuntu 22.04

· x86-64

· python 3.10.12
