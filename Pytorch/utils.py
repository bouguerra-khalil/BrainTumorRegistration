import numpy as np

def unstack_seg(seg_multiple,batch_size,classes=[0,1,2,4]):

    #Transform mono Channel multi-Class segementation into Multi Channel Mono Class Segementation file 
    #Change the multiclass segmentation Mask into a stack of binary monoclass segementation files 
    batch_size,s,r,c=seg_multiple.shape
    seg_single=np.empty((batch_size,len(classes),r,c))
    for batch in range(batch_size): 
        for idx,_class in enumerate(classes): 
            seg_single[batch,idx,:,:]=1*seg_multiple[batch,:,:,:]==_class
    return seg_single