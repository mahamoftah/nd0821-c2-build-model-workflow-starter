#!/usr/bin/env python
"""
Performs basic cleaning on the data and save the results in Weights & Biases
"""
import argparse
import logging
import wandb
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # YOUR CODE HERE     #
    ######################

    # print("Command runs successfully")
    # print("Parameters: ", args.parameter1, " ", args.parameter2, " ", args.parameter3)

    path = run.use_artifact(args.input_artifact).file()
    df = pd.read_csv(path)
    cleaned_df = df.dropna()

    artifact = wandb.Artifact(
        name="cleaned_df",
        type="cleaned_df",
        description="Data Preprocessing"
    )

    path_ = "cleaned_df.csv"
    cleaned_df.to_csv(path_, index=False)
    artifact.add_file(path_)

    run.log_artifact(artifact)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--parameter1", 
        type=int,                    ## INSERT TYPE HERE: str, float or int,
        help="param 1",                   ## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--parameter2", 
        type=int,                     ## INSERT TYPE HERE: str, float or int,
        help="param2",                       ## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--parameter3", 
        type=str,                   ## INSERT TYPE HERE: str, float or int,
        help="param 3",                   ## INSERT DESCRIPTION HERE,
        required=True
    )


    args = parser.parse_args()

    go(args)
