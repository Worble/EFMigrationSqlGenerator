import os
import subprocess
import sys
from subprocess import call


def write_err(filename, migration_name):
    sys.stderr.write(
        f'An error occurred while generating "{filename}" for migration "{migration_name}", please check the sql generated for the full exception.\n')


# make the directory to place everything in
directory = os.path.join(os.getcwd(), 'sql')

if not os.path.exists(directory):
    try:
        os.mkdir(directory)
    except OSError:
        print("Creation of the directory %s failed" % directory)
        exit()

# run the ef command to get all migrations
proc = subprocess.Popen('dotnet ef migrations list', stdout=subprocess.PIPE)
stdout, stderr = proc.communicate()
proc.wait()

# 0 is always the blank slate migrations start from
previous_migration = 0

# for each migration
for migration in stdout.splitlines():
    # decode it
    decoded_migration = migration.decode("utf8")

    # create the directory for it
    migration_directory = os.path.join(directory, decoded_migration)

    # get the internal name for ef
    efname = decoded_migration.split('_')[-1]

    # if the folder already exists, we assume this migration already exists so we skip, otherwise we make the folder
    if not os.path.exists(migration_directory):
        try:
            os.mkdir(migration_directory)
        except OSError:
            print("Creation of the directory %s failed" % directory)
            exit()

        # create the up migration
        # note: ef does give an -o (output) option to optionally specify an output file when using the script command, however the encoding on this doesn't seem to play nicely with external tools, so we make the file ourselves from the stdout
        up = os.path.join(migration_directory, "up.sql")
        with open(up, mode='w', encoding="utf8") as f:
            code = call(
                f'dotnet ef migrations script "{previous_migration}" "{efname}"', stdout=f)

            if code != 0:
                write_err("up.sql", decoded_migration)

        # create the down migration
        down = os.path.join(migration_directory, "down.sql")
        with open(down, mode='w', encoding="utf8") as f:
            code = call(
                f'dotnet ef migrations script "{efname}" "{previous_migration}"', stdout=f)

            if code != 0:
                write_err("down.sql", decoded_migration)

    # set the previous migration name to this for the next line to run from
    previous_migration = efname
