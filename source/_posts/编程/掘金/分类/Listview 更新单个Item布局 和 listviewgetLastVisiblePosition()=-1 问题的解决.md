
---
title: 'Listview 更新单个Item布局 和 listview.getLastVisiblePosition()=-1 问题的解决'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4388'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 01:36:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=4388'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>开始CSDN 和 简书文章搬家行动</p>
<ol>
<li>遇到的一个问题 ：项目中下载文件部分。在ListView 中单独更新一个进度条。
错误： 不能试用 adapter.notifyDataSetChanged(); 因为此方法会更新全部 ListView，很容易导致程序卡死，产生不好的用户体验。
正确：首先获取点击位置 ，在点击位置没有找过 ListView 的个数 之后，最重要的一步就是让点击位置 减去 ListView 在屏幕中显示的首个item的位置 ，因为：getChildAt ( int position ) 方法中position指的是当前可见区域的第几个元素。
详细代码：</li>
</ol>
<pre><code class="hljs language-java copyable" lang="java"> <span class="hljs-keyword">private</span> Handler downHandler = <span class="hljs-keyword">new</span> Handler()&#123;
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">handleMessage</span><span class="hljs-params">(Message msg)</span> </span>&#123;
<span class="hljs-keyword">if</span>(clickPosition>=lvDownLoad.getFirstVisiblePosition() &&
clickPosition <= lvDownLoad.getLastVisiblePosition()) &#123;
<span class="hljs-keyword">int</span> positionInListView = clickPosition - lvDownLoad.getFirstVisiblePosition();
ProgressBar pb = (ProgressBar) lvDownLoad.getChildAt(positionInListView)
.findViewById(R.id.pb_download);
TextView tv = (TextView) lvDownLoad.getChildAt(positionInListView)
.findViewById(R.id.tv_download_state);
<span class="hljs-keyword">switch</span> (msg.what) &#123;
<span class="hljs-keyword">case</span> <span class="hljs-number">0</span>:  <span class="hljs-comment">// 设置最大 进度条 刻度</span>
pb.setVisibility(View.VISIBLE);
tv.setText(<span class="hljs-string">"开始下载"</span>);
<span class="hljs-keyword">break</span>;
<span class="hljs-keyword">case</span> <span class="hljs-number">1</span>:  <span class="hljs-comment">// 更新进度条</span>
pb.setProgress((<span class="hljs-keyword">int</span>)(downLoadFileSize/fileSize*<span class="hljs-number">100</span>));
<span class="hljs-keyword">break</span>;
<span class="hljs-keyword">case</span> <span class="hljs-number">2</span>:  <span class="hljs-comment">// 通知下载完成</span>
pb.setVisibility(View.INVISIBLE);
tv.setText(<span class="hljs-string">"查看文件"</span>);
<span class="hljs-keyword">break</span>;
&#125;
&#125;
&#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>第一个问题解决后又发生了第二个问题（listview.getLastVisiblePosition()=-1的情况）</li>
</ol>
<p>原因：由于ListView.getLastVisiblePosition() 方法的时候，ListView 并没有加载完成。
解决方法：通过ListView .Post(new Runnable()); 在Runnable 中进行代码的 更新。</p>
<p>代码：</p>
<pre><code class="copyable">lvDownLoad.post(new Runnable() &#123;
    @Override
    public void run() &#123;
        for(int i=0;i<files.size();i++)&#123;
            if(i >= lvDownLoad.getFirstVisiblePosition() &&
                    i <= lvDownLoad.getLastVisiblePosition())&#123;
                int ii = i - lvDownLoad.getFirstVisiblePosition();

                ProgressBar pb = (ProgressBar)lvDownLoad.getChildAt(ii)
                        .findViewById(R.id.pb_download);
                TextView tv = (TextView) lvDownLoad.getChildAt(ii)
                        .findViewById(R.id.tv_download_state);
                if(GetFileSizeUtil.fileIsExists(  // 有相同文件
                        Environment.getExternalStorageDirectory().getPath()
                                +"/zcdownloadFile/"+files.get(i).getFileName()))&#123;
                    pb.setVisibility(View.INVISIBLE);
                    tv.setText("查看文件");
                &#125;else&#123; // 没有相同文件
                    pb.setVisibility(View.VISIBLE);
                    tv.setText("点击下载");
                &#125;
            &#125;
        &#125;
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            