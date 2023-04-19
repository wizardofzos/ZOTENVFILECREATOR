pre = "pre"
post = "post"


with open(pre) as prefile:
    env_pre = prefile.read().splitlines()
with open(post) as postfile:
    env_post = postfile.read().splitlines()


pre_vars = {}
post_vars = {}

for env in env_pre:
    parts = env.split('=')
    pre_vars[parts[0]] = parts[1].replace('"','')

for env in env_post:
    parts = env.split('=')
    post_vars[parts[0]] = parts[1].replace('"','')

newvars = {}

wenowant = ['LOGNAME','MAIL','PS1','SHELL','SSH_CLIENT','SSH_CONNECTION','SSH_TTY','USER','_']
for var in post_vars:
    if var in wenowant:
        continue
    if var in pre_vars:
        print(var, end=' ')
        old = pre_vars[var]
        new = post_vars[var]
        if old == new:
            print('SAME SO NO NEED')
        else:
            print(f"chec diff for {var} \n{old}\n{new}")
            added_vars = []
            oldvals = old.split(':')
            newvals = new.split(':')
            for val in newvals:
                if val not in oldvals:
                    print('is_new:', val)
                    added_vars.append(val)
            newvars[var] = f'{":".join(added_vars)}:${var}'
                
           

    else:
        print(f'{var} is NEW so keep')
        newvars[var] = post_vars[var]
    

print("ENV FILE TO SOURCE===>")
for var in newvars:
    print(f'{var}="{newvars[var]}"')

