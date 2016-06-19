#!/home/madhav/.virtualenvs/tb_dev/bin/env python
import os
import sys

if __name__ == "__main__":
    #print(os.environ.get("SAMPLE"))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskbuster.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
