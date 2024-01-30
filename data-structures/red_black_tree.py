from traitlets import TraitError


class RBNode:
    def __init__(node, key, value, nil) -> T.nil:
        node.p = nil
        node.l = nil
        node.r = nil
        node.key = key
        node.value = value
        node.is_red = True

    def __str__(node) -> str:
        return f"node: [key: {node.key}, value: {node.value}, is red?: {node.is_red}]"
    
class RBTree:
    def __init__(T):
        T.nil = RBNode(T.nil, T.nil)
        T.root = T.nil

    def preorder_walk(T, x: RBNode):
        if x != T.nil:
            print(x)
            T.preorder_walk(x.l) # recursive call on the left
            T.preorder_walk(x.r) # recursive call on the right

    def inorder_walk(T, x: RBNode):
        if x != T.nil:
            T.inorder_walk(x.l) # recursive call on the left
            print(x)
            T.inorder_walk(x.r) # recursive call on the right

    def postorder_walk(T, x: RBNode):
        if x != T.nil:
            T.postorder_walk(x.l) # recursive call on the left
            T.postorder_walk(x.r) # recursive call on the right
            print(x)
    
    def tree_search(T, key):
        x = T.root
        while x.key != key:
            if key < x.key: x = x.l
            else: x = x.r
        return x
    
    @staticmethod
    def tree_min(x: RBNode, T):
        while x.l != T.nil:
            x = x.l
        return x

    @staticmethod
    def tree_max(x: RBNode, T):
        while x.r != T.nil:
            x = x.r
        return x
    
    @staticmethod
    def tree_successor(x: RBNode, T):
        if x.r != T.nil:
            return RBTree.tree_min(x.r)
        else:
            while x.p != T.nil and x == x.p.r:
                x = x.p
            return x.p
        
    @staticmethod
    def tree_predecessor(x: RBNode, T):
        if x.l != T.nil:
            return RBTree.tree_max(x.l)
        else:
            while x.p != T.nil and x == x.p.l:
                x = x.p
            return x.p 

    def rb_insert_fixup(T, z):
        while z.p.is_red:

            if z.p == z.p.p.l:
                y = z.p.p.r

                if y.is_red:
                    z.p.p.is_red = True
                    z.p.is_red = False
                    y.is_red = False
                    z = z.p.p
                else:
                    if z != z.p.l:
                        RBTree.left_rotate(z.p)
                        z = z.p 
                    z.p.p.is_red = True
                    z.p.is_red = False
                    RBTree.right_rotate(T, z.p.p)

            else:
                y = z.p.p.l

                if y.is_red:
                    z.p.p.is_red = True
                    z.p.is_red = False
                    y.is_red = False
                    z = z.p.p
                else:
                    if z != z.p.r:
                        RBTree.right_rotate(z.p)
                        z = z.p 
                    z.p.p.is_red = True
                    z.p.is_red = False
                    RBTree.left_rotate(T, z.p.p)
        
    def tree_insert(T, z):
        x = T.root
        y = T.nil
        while x != T.nil:
            y = x
            if z.key <= x.key: x = x.l
            else: x = x.r 
        if y == T.nil:
            T.root = z
        elif z.key <= y.key: y.l = z
        else: y.r = z
        z.p = y
        T.rb_insert_fixup(z)

    def transplant(T, u, v):
        if u.p == T.nil: 
            T.root = v
        elif u.p.l == u:
            u.p.l = v
        else:
            u.p.r = v
        if v != T.nil: 
            v.p = u.p 

    def tree_delete(T, z):
        if z.l == T.nil:
            T.transplant(z, z.r)
        elif z.r == T.nil:
            T.transplant(z, z.l)
        else:
            y = RBTree.tree_successor(z)
            if y != z.r:
                T.transplant(y, y.r)
                y.r = z.r
                z.r.p = y
            T.transplant(z, y)
            y.l = z.l
            z.l.p = y

    @staticmethod
    def left_rotate(T, x):
        y = x.r
        x.r = y.l
        if y.l:
            y.l.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x.p.l == x:
            x.p.l = y
        else:
            x.p.r = y
        y.l = x
        x.p = y

    @staticmethod
    def right_rotate(T, x):
        y = x.l
        x.l = y.r
        if y.r:
            y.r.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x.p.l == x:
            x.p.l = y
        else:
            x.p.r = y
        y.r = x
        x.p = y