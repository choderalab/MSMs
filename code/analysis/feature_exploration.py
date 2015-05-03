def describe_features(self, traj):
    """Return a Pandas Dataframe describing the features."""
    x = []
    for a in self.types:
        func = getattr(md, 'compute_%s' % a)
        aind, y = func(traj)
        n = len(aind)
        
        aind = aind[:, 1]
        
        resnames = [traj.top.atom(i).residue.name for i in aind]
        resSeq = [traj.top.atom(i).residue.resSeq for i in aind]
        resid = [traj.top.atom(i).residue.index for i in aind]
        bigclass = ["dihedral"] * n
        smallclass = [a] * n
        
        if self.sincos:
            #x.extend([np.sin(y), np.cos(y)])
            resnames = resnames * 2
            resSeq = resSeq * 2
            resid = resid * 2
            trig = (["sin"] * n) + (["cos"] * n)
            bigclass = bigclass * 2
            smallclass = smallclass * 2
        else:
            trig = ["nosincos"] * n
        
        for i in range(len(resnames)):
            d_i = dict(resname=resnames[i], resSeq=resSeq[i], resid=resid[i], trig=trig[i], bigclass=bigclass[i], smallclass=smallclass[i])
            x.append(d_i)
    
    return x
