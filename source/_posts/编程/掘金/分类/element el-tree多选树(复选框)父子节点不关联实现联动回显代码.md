
---
title: 'element el-tree多选树(复选框)父子节点不关联实现联动回显代码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2791'
author: 掘金
comments: false
date: Fri, 14 May 2021 22:19:24 GMT
thumbnail: 'https://picsum.photos/400/300?random=2791'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>属性check-strictly：在显示复选框的情况下，是否严格的遵循父子不互相关联的做法，默认为 false。</strong></p>
<p><strong>实现的功能：</strong></p>
<pre><code class="copyable">1、点击根（父）节点，下面的子节点全部勾选上

2、点击子节点父节点勾选上（嵌套多层父节点自动递归往上查找）

3、已勾选父节点下的子节点全部取消勾选，父节点就取消勾选。

4、如嵌套多层父节点默认递归往上查找，直到找到父级节点下的全部同级子节点不是全取消勾选状态的。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意事项：</strong>
1、方法里的parent不要修改</p>
<p>2、parentId和children根据你自己获取到的参数修改</p>
<p><strong>方法在最下面可以直接翻到底</strong></p>
<pre><code class="copyable">获取最终选中id值this.$refs.tree.getCheckedKeys().concat(this.$refs.tree.getHalfCheckedKeys())返回数组
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><template>
    <div>
        <el-tree ref="tree"
                 :data="treeMenus"
                 :props="multiProps"
                 :show-checkbox="true"
                 node-key="id"
                 highlight-current
                 :expand-on-click-node="true"
                 :default-checked-keys="checkedId"
                 :check-strictly="true"
                 @check="clickDeal">
        </el-tree>
    </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">return &#123;
             checkedId: [],
             treeMenus: [&#123;
                    id: 1,
                    parentId: -1,
                    label: '一级 1',
                    children: [&#123;
                        id: 4,
                        parent: 1,
                        label: '二级 1-1',
                        children: [&#123;
                            id: 9,
                            parentId: 4,
                            label: '三级 1-1-1',
                            children: [&#123;
                                id: 1000,
                                parentId: 9,
                                label: '三级 1000-1-1',
                                children: []
                            &#125;, &#123;
                                id: 1001,
                                parentId: 9,
                                label: '三级 1001-1-1',
                                children: [&#123;
                                    id: 2000,
                                    parentId: 1001,
                                    label: '三级 2000-1-1',
                                    children: []
                                &#125;,&#123;
                                    id: 2001,
                                    parentId: 1001,
                                    label: '三级 2001-1-1',
                                    children: []
                                &#125;]
                            &#125;]
                        &#125;, &#123;
                            id: 10,
                            parentId: 4,
                            label: '三级 1-1-2',
                            children: []
                        &#125;]
                    &#125;, &#123;
                        id: 20,
                        parentId: 1,
                        label: '123',
                        children: []
                    &#125;, &#123;
                        id: 25,
                        parentId: 1,
                        label: '12456',
                        children: []
                    &#125;]
                &#125;, &#123;
                    parentId: -1,
                    id: 2,
                    label: '一级 2',
                    children: [&#123;
                        parentId: 2,
                        id: 5,
                        label: '二级 2-1',
                        children: []
                    &#125;, &#123;
                        parentId: 2,
                        id: 6,
                        label: '二级 2-2',
                        children: []
                    &#125;]
                &#125;, &#123;
                    parentId: -1,
                    id: 3,
                    label: '一级 3',
                    children: [&#123;
                        parentId: 3,
                        id: 7,
                        label: '二级 3-1',
                        children: []
                    &#125;, &#123;
                        parentId: 3,
                        id: 8,
                        label: '二级 3-2',
                        children: []
                    &#125;]
                &#125;],
                multiProps: &#123;
                    children: 'children',
                    label: 'label'
                &#125;
            &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">methods: &#123;
           clickDeal(currentObj, treeStatus)&#123;
                this.clickCheck(currentObj, treeStatus,this.$refs.tree)
            &#125;,

            /**
             * 树形菜单复选框父子节点不关联实现父子节点联动回显
             *
             * @see selectedParent - 处理父节点为选中
             * @see uniteChildSame - 处理子节点为相同的勾选状态
             * @see removeParent   - 子节点全没选中取消父级的选中状态
             *
             * @param &#123;Object&#125; currentObj - 当前勾选节点的对象
             * @param &#123;Object&#125; treeStatus - 树目前的选中状态对象
             * @param &#123;Object&#125; ref - this.$refs.xxx
             **/
            clickCheck(currentObj, treeStatus, ref) &#123;
                // 用于：父子节点严格互不关联时，父节点勾选变化时通知子节点同步变化，实现单向关联。
                let selected = treeStatus.checkedKeys.indexOf(currentObj.id); // -1未选中

                // 选中
                if (selected !== -1) &#123;
                    // 子节点只要被选中父节点就被选中
                    this.selectedParent(currentObj, ref);
                    // 统一处理子节点为相同的勾选状态
                    this.uniteChildSame(currentObj, true, ref);
                &#125; else &#123;
                    // 取消子节点的选中状态触发
                    if (currentObj.parentId !== -1) &#123;
                        this.removeParent(currentObj, ref);
                    &#125;

                    // 未选中 处理子节点全部未选中
                    if (currentObj.children.length !== 0) &#123;
                        this.uniteChildSame(currentObj, false, ref);
                    &#125;
                &#125;
            &#125;,

            /**   统一处理子节点为相同的勾选状态  **/
            uniteChildSame(treeList, isSelected, ref) &#123;
                let treeListData = treeList.children;
                let len = treeListData.length;

                ref.setChecked(treeList.id, isSelected);

                for (let i = 0; i < len; i++) &#123;
                    this.uniteChildSame(treeListData[i], isSelected, ref);
                &#125;
            &#125;,

            /**    统一处理父节点为选中    **/
            selectedParent(currentObj, ref) &#123;
                let currentNode = ref.getNode(currentObj);
                if (currentNode.parent.key !== undefined) &#123;
                    ref.setChecked(currentNode.parent, true);
                    return this.selectedParent(currentNode.parent, ref);
                &#125;
            &#125;,

            /**    子节点全没选中取消父级的选中状态   **/
            removeParent(currentObj, ref) &#123;
                let a = 0;
                let b = 0;
                let currentNode = ref.getNode(currentObj);
                if (currentNode.parent !== null) &#123;
                    if (currentNode.parent.key !== undefined) &#123;
                        ref.setChecked(currentNode.parent, true); //根节点
                        this.removeParent(currentNode.parent, ref); //递归判断子节点
                    &#125;
                &#125;

                //不为0表示为父节点
                if (currentNode.childNodes.length !== 0) &#123;

                    //循环判断父节点下的子节点
                    for (let i = 0; i < currentNode.childNodes.length; i++) &#123;

                        //判断父节点下的子节点是否全为false
                        if (currentNode.childNodes[i].checked === false) &#123;
                            ++a;

                            //a === currentNode.childNodes.length 表明子节点全为false
                            if (a === currentNode.childNodes.length) &#123;

                                //等于 undefined 跳过,不等于继续执行
                                if (currentNode.childNodes[i].parent.key !== undefined) &#123;
                                    ref.setChecked(currentNode.childNodes[i].parent, false); //父元素设置为false
                                    //循环上级父节点下的子节点
                                    for (let i = 0; i < currentNode.parent.childNodes.length; i++) &#123;

                                        //判断父节点下的子节点是否全为false
                                        if (currentNode.parent.childNodes[i].checked === false) &#123;
                                            ++b;

                                            //b === currentNode.parent.childNodes.length 表明子节点全为false
                                            if (b === currentNode.parent.childNodes.length) &#123;
                                                ref.setChecked(currentNode.parent.key, false); //父元素设置为false
                                                return this.removeParent(currentNode.parent, ref); //继续递归循环判断
                                            &#125;
                                        &#125;
                                    &#125;
                                &#125;
                            &#125;
                        &#125;
                    &#125;
                &#125;
            &#125;,
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>本代码修改自：<a href="https://blog.csdn.net/Beam007/article/details/87858291" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/Beam007/art…</a></p>
</blockquote></div>  
</div>
            