
---
title: 'vue子组件向父组件传值的两种方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6228'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 20:19:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=6228'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>一、子组件主动触发事件将数据传递给父组件</strong>
1、在子组件上绑定某个事件以及事件触发的函数子组件代码</p>
<pre><code class="copyable"><template>
<div>
    <Tree :data="treeData" show-checkbox ref="treeData"></Tree>
    <Button type="success" @click="submit"></Button>
</div>  
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>事件在子组件中触发的函数：</p>
<pre><code class="copyable">submit()&#123;
  this.$emit('getTreeData',this.$refs.treeData.getCheckedNodes());
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在父组件中绑定触发事件：</p>
<pre><code class="copyable"><AuthTree  @getTreeData='testData'></AuthTree>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件触发函数显示子组件传递的数据：</p>
<pre><code class="copyable">testData(data)&#123;
      console.log("parent");
      console.log(data)
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>二、不需要再子组件中触发事件（如点击按钮，create（）事件等等）</strong></p>
<p>这种方式要简单得多，子组件中绑定ref</p>
<pre><code class="copyable"><template>
<div>
<Tree :data="treeData" show-checkbox ref="treeData"></Tree>
</div>  
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在子组件中定义一个函数，这个函数是父组件可以直接调用的。函数的返回值定义为我们需要的数据。</p>
<pre><code class="copyable">getData()&#123;
        return this.$refs.treeData.getCheckedNodes()
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再父组件注册子组件后绑定ref，调用子组件的函数获取数据：</p>
<pre><code class="copyable"><AuthTree ref="authTree"></AuthTree>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件函数调用：</p>
<pre><code class="copyable">this.$refs.authTree.getData()
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            