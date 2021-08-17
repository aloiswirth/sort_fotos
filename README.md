# Very first own documentation along with the code
> Summary description here.


This file will become your README and also the index of your documentation.

## Install

pip install your_project_name

## How to use

Fill me in please! Don't forget code examples:

```
1+1
```




    2



The next version of my test documentation

Necessary onetime preparation for using nbdev:
https://jekyllrb.com/docs/installation/windows/#installation-via-bash-on-windows-10
*Attention*: During this procedure I ran several times in error messages due to authorization. Therefore at the end I changed the authorizations of 
'/usr/local/' and '/var/lib/gems' to be readable and writeable for all users. 
The first step is 
- 'gem update'
This takes around an hour. Please be patient.

The seconde step is: 
- 'gem install jekyll bundler'
This also took 30 minutes.

Necessary steps for a new nbdev project:

0. for your project enable the Github pages
1. nbdev_new for any project
2. Edit the settings.ini
3. nbdev_install_git_hooks
4. write the code
5. nbdev_build_libs
6. Edit index.ipynb and include the module name from the settings.ini
7. eventually run nbdev_test_nbs to test the notebooks
8. Then run 
    make docs_serve
    or later run only
    nbdev_build_docs
9. git add, commit and push

```
%lsmagic
```




    Available line magics:
    %alias  %alias_magic  %autocall  %automagic  %autosave  %bookmark  %cat  %cd  %clear  %colors  %config  %connect_info  %cp  %debug  %dhist  %dirs  %doctest_mode  %ed  %edit  %env  %gui  %hist  %history  %killbgscripts  %ldir  %less  %lf  %lk  %ll  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %lsmagic  %lx  %macro  %magic  %man  %matplotlib  %mkdir  %more  %mv  %notebook  %page  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %pip  %popd  %pprint  %precision  %profile  %prun  %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %qtconsole  %quickref  %recall  %rehashx  %reload_ext  %rep  %rerun  %reset  %reset_selective  %rm  %rmdir  %run  %save  %sc  %set_env  %shell  %store  %sx  %system  %tb  %tensorflow_version  %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode
    
    Available cell magics:
    %%!  %%HTML  %%SVG  %%bash  %%bigquery  %%capture  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%shell  %%svg  %%sx  %%system  %%time  %%timeit  %%writefile
    
    Automagic is ON, % prefix IS NOT needed for line magics.


