# cdm-testdata
IMMA1 example files used for the testing suite of `cdm_reader_mapper`

## Contributing
In order to add a new dataset to the `cdm_reader_mapper` testing data, please ensure you perform the following:

1. Create a new branch: `git checkout -b my_new_testdata_branch`
2. Place your dataset within an appropriate subdirectory (or create a new one: `mkdir testdata_contribution`).
3. Run the md5 checksum generation script: `python make_check_sums.py`
4. Commit your changes: `git add testdata_contribution && git commit -m "added my_new_testdata"`
5. Open a Pull Request.

To modify an existing dataset, be sure to remove the existing checksum file before running the `make_check_sums.py` script.


## Versioning
When updating a dataset in `cdm-testdata` using a development branch and Pull Request,
once changes have been merged to the `main` branch, you should tag a new version of `cdm-testdata`. 

The version tag of `cdm-testdata` should follow a [calendar versioning](https://calver.org/) scheme
(i.e. version string follows from `vYYYY.MM.DD-r#`) reflecting the date of the tag creation, with modifiers if required.

## Credits

This package was build according to [xclim-testdata](https://github.com/Ouranosinc/xclim-testdata).
