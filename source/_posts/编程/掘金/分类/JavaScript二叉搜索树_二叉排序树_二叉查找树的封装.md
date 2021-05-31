
---
title: 'JavaScript二叉搜索树_二叉排序树_二叉查找树的封装'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cae979ecbc084a389363ce5b1d075fb7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 28 May 2021 00:56:38 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cae979ecbc084a389363ce5b1d075fb7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>最近在学习二叉树，复盘和总结一下这个东东。不说了都是泪，奉劝各位在学校的课程上认认真真学习数据结构，这是个好东西</p>
<h2 data-id="heading-1">正文</h2>
<p>二叉搜索树/二叉排序树/二叉查找树，英文:BST,Binary Search tree，其实这三个名字是同一个二叉树，这里就用二叉搜索树来说。</p>
<h3 data-id="heading-2">二叉搜索树</h3>
<p>二叉搜索树是什么，这可能要结合性质(生成条件)来说</p>
<pre><code class="copyable">1.二叉搜索树是一个二叉树，可以为空
2.如果不为空，需要满足以下的性质
       1. 非空左子树的所有键值小于根节点的键值
       2. 非空右子树的所有键值大于根节点的键值
       3. 左、 右子树本身也是二叉搜索树
总结的话就是，对于每一个节点来说，键值小的的左边，键值大的在右边(小左大右)。

我们来看一张图，可以更好的理解
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cae979ecbc084a389363ce5b1d075fb7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">以根节点5为例，比它小的都在左子树，比它大的都在右子树
其他的子节点也一样，这就是一个二叉搜索树
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">代码实现</h3>
<p>结合上面的图我们可以看到，其实二叉树是由节点构成的，节点里有键值和指向左右的两个箭头，所以可以看成一个节点有三个属性,我们先创建一个BinarySearchTree类</p>
<h4 data-id="heading-4">BinarySearchTree类</h4>
<pre><code class="copyable"> function BinarySearchTree() &#123;
             //创建一个节点类
            function Node(key) &#123;
                // 一个节点有三个属性，一个是键，另外两个是指向左右两边的节点
                this.key = key
                this.left = null
                this.right = null
            &#125;

            //根节点
            this.root = null
     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">方法</h4>
<p>接下来就是方法，下面的方法用了递归思想，第一个是插入节点的方法</p>
<h5 data-id="heading-6">insert(key): 向树中插入一个新的键</h5>
<pre><code class="copyable">原理:通过递归的方法，新Node和根节点，其他节点进行比较，新Node大于就放右边，小于就放左边，
每个节点都要比较，直到为空
    BinarySearchTree.prototype.insert = function (key) &#123;
        // 创建一个要插入的键
        var newNode = new Node(key)

        // 先判断是否有根节点，如果没有，那插入的键就成为根节点
        if (this.root == null) &#123;
            this.root = newNode
        &#125; else &#123;
            this.insertNode(this.root, newNode)
        &#125;

    &#125;
    // 递归函数
    BinarySearchTree.prototype.insertNode = function (node, newNode) &#123;
        // node是指要比较的那个节点

        if (newNode.key > node.key) &#123; //向右查找
            // 因为要插入到右边，那就要判断右边是否有节点

            if (node.right == null) &#123; //如果没有，插入的节点就成为右节点
                node.right = newNode
            &#125; else &#123; //如果有，那就需要在进行递归判断，再次调用这个函数，直到上一步骤失败
                this.insertNode(node.right, newNode)
            &#125;
        &#125; else &#123; //向左查找        操作同上
            if (node.left == null) &#123;
                node.left = newNode
            &#125; else &#123;
                this.insertNode(node.left, newNode)
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里先不测试，结合后面的遍历一起测试</p>
<h4 data-id="heading-7">preOrderTraverse: 通过先序遍历遍历所有节点</h4>
<p>理解其中一个，其他的遍历也差不多会明白</p>
<pre><code class="copyable">原理：先访问根节点，在访问其左子树，在访问右子树
    BinarySearchTree.prototype.preOrderTraverse = function (handler) &#123;
        // 从根节点开始遍历
        this.preOrderTraverseNode(this.root, handler)
    &#125;
    // 先序遍历递归函数
    BinarySearchTree.prototype.preOrderTraverseNode = function (node, handler) &#123;
        if (node != null) &#123; //判断经过的节点是否为空
            handler(node.key) 
            //因为是遍历，所有要看到结果，用一个函数来处理，将经过的节点加入到字符串
    
            //如果有左节点，在执行我们的遍历函数，将节点加入到字符串中，一直到左节点为空
            this.preOrderTraverseNode(node.left, handler)

            // 如果最后一个左节点为叶子节点，就在判断它是否还有右节点
            // 如果有，就继续递归执行函数。
            // 如果没有，那么当前节点就完成了上一次递归调用，开始判断上一个节点的递归函数
            this.preOrderTraverseNode(node.right, handler)

        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">inOrderTraverse: 通过中序(升序)遍历遍历所有节点</h4>
<p>其实就只是改变调用顺序，后序遍历也是</p>
<pre><code class="copyable">原理:先访问左子树，在访问根节点，在访问右子树，对树进行排序操作如果是数字的话，就小到大排列
    BinarySearchTree.prototype.inOrderTraverse = function (handler) &#123;
        this.inOrderTraverseNode(this.root, handler)
        // 为什么是this.root，因为只能从根节点开始进入
    &#125;
    // 中序遍历递归函数
    BinarySearchTree.prototype.inOrderTraverseNode = function (node, handler) &#123;
        if (node != null) &#123;
            // 从根节点开始进入，如果他有左节点，就会不断进行递归，会一直遍历到最左叶子节点

            // 到了最左叶子节点，就结束将该节点加入到字符串中，在判断是否有右节点
            // 没有就回到上个函数，那么函数里的左节点判断就结束麻，将当前节点加入字符串，在判断右边
            // ....
            // 如果进入到一个新支，有左节点，有因为递归调用，所有函数又来到最左叶子节点

            //可以把根节点的左边看成一个左节点的函数判断，所有判断结束，中间就打印根节点，所以是中序遍历
            this.inOrderTraverseNode(node.left, handler)
            handler(node.key)
            this.inOrderTraverseNode(node.right, handler)
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">postOrderTraverse: 通过后序遍历遍历所有节点</h4>
<p>这里就不在注释说明了</p>
<pre><code class="copyable">原理:先访问左子树，在访问右子树，在访问根节点
    BinarySearchTree.prototype.postOrderTraverse = function (handler) &#123;
        this.postOrderTraverseNode(this.root, handler)
    &#125;
    BinarySearchTree.prototype.postOrderTraverseNode = function (node, handler) &#123;
        if (node != null) &#123;
            // 其实道理差不多，就不在说了
            this.postOrderTraverseNode(node.left, handler)
            this.postOrderTraverseNode(node.right, handler)
            handler(node.key)
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">min: 返回树中最小的值键</h4>
<p>这个没啥好说的，就是你想的那样</p>
<pre><code class="copyable">BinarySearchTree.prototype.min = function () &#123;
        var node = this.root //获取根节点
        // var key=null    创建一个key来返回值
        // 依次向右不断查找，因为node一直有值，所以会循环，直到node=null
        while (node != null) &#123;
            key = node.key
            node = node.left
        &#125;
        return key
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">max: 返回树中最大的值键</h4>
<pre><code class="copyable">    BinarySearchTree.prototype.max = function () &#123;
        var node = this.root //
        var key = null
        while (node != null) &#123;
            key = node.key
            node = node.right
        &#125;
        return key
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">search(key): 在树中查找一个键，如果节点存在，返回true</h4>
<pre><code class="copyable">BinarySearchTree.prototype.search = function (key) &#123;
        return this.searchNode(this.root, key)
    &#125;
//递归
BinarySearchTree.prototype.searchNode = function (node, key) &#123;
        if (node === null) &#123; //判断根节点是否为空，以及后面递归的节点
            return false
        &#125;

        if (key > node.key) &#123;
            // 递归之后，key继续和后面的节点比较
            return this.searchNode(node.right, key)
        &#125; else if (key < node.key) &#123;
            return this.searchNode(node.left, key)
        &#125; else &#123;
            return true
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">测试</h3>
<pre><code class="copyable">var bst = new BinarySearchTree()
    // 测试插入
    bst.insert(7)
    bst.insert(66)
    bst.insert(5)
    bst.insert(17)
    bst.insert(11)
    bst.insert(3)

    // 测试先序
    let res1 = ''
    bst.preOrderTraverse(function (key) &#123;
        res1 += key + ' '
    &#125;)
    console.log(res1)
    //测试中序
    res2 = ''
    bst.inOrderTraverse(function (key) &#123;
        res2 += key + ' '
    &#125;)
    console.log(res2)
    //测试后序
    res2 = ''
    bst.postOrderTraverse(function (key) &#123;
        res2 += key + ' '
    &#125;)
    console.log(res2)
    //大小
    console.log(bst.min())
    console.log(bst.max())
    //查找
    console.log(bst.search(2))
    console.log(bst.search(66))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>树图和结果图</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e1b6b385ade4c098dea9e29adc1bfc6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">总结</h2>
<p>其实还有一个方法，就是remove，这个方法有点难，到时候在写一篇单独发</p>
<p>想出二叉搜索树的真是神仙,牛皮。没啥总结，我觉得注释就是我的总结</p></div>  
</div>
            