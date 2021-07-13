
---
title: 'vue 实现鼠标移入移出表格，显示影藏图标, 并弹出提示内容'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff4f31e54b0647139dc49645fef4ffd5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 22:04:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff4f31e54b0647139dc49645fef4ffd5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>效果：</p>
<ol>
<li>table代码：</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff4f31e54b0647139dc49645fef4ffd5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"><el-table :data="tableData" ref="multipleTable" class="multTable" 
    row-key="id"  @cell-mouse-enter="mouseOver"  @cell-mouse-leave="mouseLeave">
    <el-table-column type="index" label="优先级" width="100px">
        <template slot-scope="scope">
            <i class="iconfont" v-show="scope.row.showIcon">&#xe6ec;</i>
            <el-popover
                placement="top-start"
                width="200"
                trigger="hover"
                content="我是提示内容">
                <el-button slot="reference" type="text">&#123;&#123; scope.$index + 1 &#125;&#125;</el-button>
             </el-popover>
         </template>
      </el-table-column>
 <el-table>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>重点： @cell-mouse-enter鼠标移入 @cell-mouse-leave="mouseLeave"鼠标移出</li>
<li>初始化表格数据，定义showIcon字段为false</li>
</ol>
<pre><code class="copyable">methods：&#123;
    this.dataList.forEach((item) => &#123;
        item.showIcon = false
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>自定义弹出提示内容：</li>
</ol>
<pre><code class="copyable"><el-popover
    placement="top-start"
    width="200"
    trigger="hover"
    content="我是提示内容">
    <el-button slot="reference" type="text">&#123;&#123; scope.$index + 1 &#125;&#125;</el-button>
 </el-popover>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>鼠标移入、移除事件：</li>
</ol>
<pre><code class="copyable">methods：&#123;
    mouseOver(row) &#123;
        row.showIcon = true
    &#125;,
    mouseLeave(row) &#123;
        row.showIcon = false
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            