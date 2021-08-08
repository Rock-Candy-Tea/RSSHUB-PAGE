
---
title: 'Linux crontab使用说明'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=62'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 01:31:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=62'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>crontab</code>是用来定期自动执行脚本的命令</p>
<h2 data-id="heading-0">常用参数</h2>
<ul>
<li><code>crontab -l</code>列出所有定期自动执行的任务</li>
<li><code>crontab -e</code>编辑所有定期自动执行的任务</li>
</ul>
<p><strong>任务格式</strong></p>
<pre><code class="copyable"> 执行周期 脚本路径 日志输出
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如：</p>
<pre><code class="copyable"> */5 * * * * /usr/local/agenttools/agent/check_tmp_agent.sh >/dev/null 2>&1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">执行周期</h3>
<pre><code class="copyable"> *    *    *    *    *
 -    -    -    -    -
 |    |    |    |    |
 |    |    |    |    +----- week (0 - 6) (sunday 0)
 |    |    |    +---------- month (1 - 12) 
 |    |    +--------------- day (1 - 31)
 |    +-------------------- hour (0 - 23)
 +------------------------- minute (0 - 59)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了具体数值之外，可能会用到的特殊字符：</p>
<ul>
<li><code>*</code>：取任意可能的值</li>
<li><code>,</code>：指定一个列表的取值，例如，<code>10,12,14,20</code></li>
<li><code>-</code>：指定一个范围的取值，例如，<code>12-14</code></li>
<li><code>/</code>：指定步长的取值，也就是时间间隔频率，例如，<code>*/30</code>如果写在<code>minute</code>字段，表示每30分钟执行一次</li>
</ul>
<h3 data-id="heading-2">脚本路径</h3>
<p>脚本的绝对路径。</p>
<pre><code class="copyable"> /usr/local/agenttools/agent/check_tmp_agent.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">日志输出</h3>
<pre><code class="copyable"> >/dev/null 2>&1
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>/dev/null</code>代表设备空文件</li>
<li>标准输入<code>stdin</code>的文件描述符为<code>0</code></li>
<li>标准输出<code>stdout</code>的文件描述符为<code>1</code></li>
<li>标准错误<code>stderr</code>的文件描述符为<code>2</code></li>
</ul>
<p><strong>不输出日志</strong></p>
<pre><code class="copyable"> > /dev/null 2>&1
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>标准输出日志</strong></p>
<pre><code class="copyable"> > /tmp/out.log
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或</p>
<pre><code class="copyable"> 1> /tmp/out.log
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>标准错误日志</strong></p>
<pre><code class="copyable"> 2> /tmp/err.log
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>标准输出+标准错误日志</strong></p>
<pre><code class="copyable"> > /tmp/total.log 2>&1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>\</p></div>  
</div>
            