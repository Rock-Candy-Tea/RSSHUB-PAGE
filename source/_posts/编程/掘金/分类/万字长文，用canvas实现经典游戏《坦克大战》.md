
---
title: '万字长文，用canvas实现经典游戏《坦克大战》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aac051396a0446ebac688278e7d51f4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 00:28:33 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aac051396a0446ebac688278e7d51f4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
<h3 data-id="heading-0">写在前面</h3>
<p>前面我们实现了一个简单的canvas库 <a href="https://juejin.cn/post/7130894865440702478" target="_blank" title="https://juejin.cn/post/7130894865440702478">100行代码写个canvas库</a> ，也用它做了几个小Demo</p>
<ul>
<li><a href="https://juejin.cn/post/7130897054921916452" target="_blank" title="https://juejin.cn/post/7130897054921916452">用canvas实现一个雪碧图制作工具</a></li>
<li><a href="https://juejin.cn/post/7130897368915902494" target="_blank" title="https://juejin.cn/post/7130897368915902494">用canvas实现一个简易流程图</a></li>
<li><a href="https://juejin.cn/post/7132311241606823966" target="_blank" title="https://juejin.cn/post/7132311241606823966">实现canvas的元素动画</a></li>
<li><a href="https://juejin.cn/post/7132409266803048478" target="_blank" title="https://juejin.cn/post/7132409266803048478">实现canvas元素的补间动画</a></li>
<li><a href="https://juejin.cn/post/7136089618331631653" target="_blank" title="https://juejin.cn/post/7136089618331631653">实现无限循环的游戏背景</a></li>
<li><a href="https://juejin.cn/post/7140582830773370887" target="_blank" title="https://juejin.cn/post/7140582830773370887">用canvas实现经典游戏《跳上一百层》</a></li>
</ul>
<p>看到前面活动里的奖励有小霸王游戏机，瞬间勾起了小时候的回忆，所以就实现了这个坦克大战，这里把实现过程整理出来。</p>
<p><span href="https://code.juejin.cn/pen/7140916117526020109" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7140916117526020109" data-src="https://code.juejin.cn/pen/7140916117526020109" style="display: none" loading="lazy"></iframe></span></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fheyach.github.io%2Ftankonline%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://heyach.github.io/tankonline/" ref="nofollow noopener noreferrer">在线体验传送门</a></p>
<h3 data-id="heading-1">回忆</h3>
<p>经过短暂的回忆后，这个游戏的玩法和机制大概有下面这些</p>
<ul>
<li>墙（土砖，铁砖，水，草地）</li>
<li>敌方坦克（种类很多，红坦克打死会出道具）</li>
<li>道具（坦克加命，时钟定身，铁锹保护基地，炸弹清场，星星升级坦克，安全帽无敌）</li>
<li>我方坦克</li>
<li>城堡</li>
<li>提示信息（敌方还有多少坦克，我方还剩多少条命）</li>
<li>其他隐藏机制</li>
</ul>
<h3 data-id="heading-2">初始化游戏场景</h3>
<p>以<code>60x60</code>的方块，搭建一个<code>13x13</code>的场景</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> s2 = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Stage</span>(<span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"stage"</span>), <span class="hljs-number">780</span>, <span class="hljs-number">780</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>游戏里的每个砖块都是由<code>4</code>个小砖块组成的，所以可以打掉一个角，这里为了节省时间，最小单位是<code>60x60</code>的方块，我们先来实现<code>土砖</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Brick</span> &#123;
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params">option</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> = option.<span class="hljs-property">x</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> = option.<span class="hljs-property">y</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span> = option.<span class="hljs-property">w</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span> = option.<span class="hljs-property">h</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">type</span> = <span class="hljs-string">"Brick"</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Image</span>()
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span>.<span class="hljs-property">src</span> = <span class="hljs-string">"./tuzhuan.png"</span>
    &#125;

    <span class="hljs-title function_">draw</span>(<span class="hljs-params">ctx</span>) &#123;
        ctx.<span class="hljs-title function_">drawImage</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span>);
    &#125;
    <span class="hljs-title function_">destroy</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">parent</span>.<span class="hljs-title function_">remove</span>(<span class="hljs-variable language_">this</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后根据第一关的分布，完成初始化</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 关卡</span>
<span class="hljs-keyword">let</span> shut = &#123;
<span class="hljs-comment">// 第一关</span>
    <span class="hljs-attr">one</span>: [[<span class="hljs-number">60</span>, <span class="hljs-number">60</span>],[<span class="hljs-number">180</span>, <span class="hljs-number">60</span>],[<span class="hljs-number">300</span>,<span class="hljs-number">60</span>],[<span class="hljs-number">420</span>,<span class="hljs-number">60</span>],[<span class="hljs-number">540</span>,<span class="hljs-number">60</span>],[<span class="hljs-number">660</span>,<span class="hljs-number">60</span>],
        [<span class="hljs-number">60</span>, <span class="hljs-number">120</span>],[<span class="hljs-number">180</span>, <span class="hljs-number">120</span>],[<span class="hljs-number">300</span>,<span class="hljs-number">120</span>],[<span class="hljs-number">420</span>,<span class="hljs-number">120</span>],[<span class="hljs-number">540</span>,<span class="hljs-number">120</span>],[<span class="hljs-number">660</span>,<span class="hljs-number">120</span>],
        [<span class="hljs-number">60</span>, <span class="hljs-number">180</span>],[<span class="hljs-number">180</span>, <span class="hljs-number">180</span>],[<span class="hljs-number">300</span>,<span class="hljs-number">180</span>],[<span class="hljs-number">420</span>,<span class="hljs-number">180</span>],[<span class="hljs-number">540</span>,<span class="hljs-number">180</span>],[<span class="hljs-number">660</span>,<span class="hljs-number">180</span>],
        [<span class="hljs-number">60</span>, <span class="hljs-number">240</span>],[<span class="hljs-number">180</span>, <span class="hljs-number">240</span>],[<span class="hljs-number">540</span>,<span class="hljs-number">240</span>],[<span class="hljs-number">660</span>,<span class="hljs-number">240</span>],
        [<span class="hljs-number">300</span>, <span class="hljs-number">300</span>],[<span class="hljs-number">420</span>,<span class="hljs-number">300</span>],
        [<span class="hljs-number">0</span>, <span class="hljs-number">360</span>],[<span class="hljs-number">120</span>, <span class="hljs-number">360</span>],[<span class="hljs-number">180</span>,<span class="hljs-number">360</span>],[<span class="hljs-number">540</span>,<span class="hljs-number">360</span>],[<span class="hljs-number">600</span>,<span class="hljs-number">360</span>],[<span class="hljs-number">720</span>,<span class="hljs-number">360</span>],
        [<span class="hljs-number">0</span>, <span class="hljs-number">420</span>],[<span class="hljs-number">720</span>,<span class="hljs-number">420</span>],
        [<span class="hljs-number">0</span>, <span class="hljs-number">480</span>],[<span class="hljs-number">720</span>,<span class="hljs-number">480</span>],
        [<span class="hljs-number">60</span>, <span class="hljs-number">480</span>],[<span class="hljs-number">180</span>, <span class="hljs-number">480</span>],[<span class="hljs-number">540</span>,<span class="hljs-number">480</span>],[<span class="hljs-number">660</span>,<span class="hljs-number">480</span>],
        [<span class="hljs-number">60</span>, <span class="hljs-number">540</span>],[<span class="hljs-number">180</span>, <span class="hljs-number">540</span>],[<span class="hljs-number">540</span>,<span class="hljs-number">540</span>],[<span class="hljs-number">660</span>,<span class="hljs-number">540</span>],
        [<span class="hljs-number">60</span>, <span class="hljs-number">600</span>],[<span class="hljs-number">180</span>, <span class="hljs-number">600</span>],[<span class="hljs-number">540</span>,<span class="hljs-number">600</span>],[<span class="hljs-number">660</span>,<span class="hljs-number">600</span>],
        [<span class="hljs-number">60</span>, <span class="hljs-number">660</span>],[<span class="hljs-number">180</span>, <span class="hljs-number">660</span>],[<span class="hljs-number">540</span>,<span class="hljs-number">660</span>],[<span class="hljs-number">660</span>,<span class="hljs-number">660</span>],
        [<span class="hljs-number">300</span>, <span class="hljs-number">420</span>],[<span class="hljs-number">420</span>,<span class="hljs-number">420</span>],
        [<span class="hljs-number">300</span>, <span class="hljs-number">480</span>],[<span class="hljs-number">360</span>,<span class="hljs-number">480</span>],[<span class="hljs-number">420</span>,<span class="hljs-number">480</span>],
        [<span class="hljs-number">300</span>, <span class="hljs-number">540</span>],[<span class="hljs-number">420</span>,<span class="hljs-number">540</span>],
        [<span class="hljs-number">300</span>, <span class="hljs-number">660</span>],[<span class="hljs-number">360</span>,<span class="hljs-number">660</span>],[<span class="hljs-number">420</span>,<span class="hljs-number">660</span>],
        [<span class="hljs-number">300</span>, <span class="hljs-number">720</span>],[<span class="hljs-number">420</span>,<span class="hljs-number">720</span>],]
&#125;,
<span class="hljs-keyword">let</span> tuzhuans = shut.<span class="hljs-property">one</span>
tuzhuans.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-keyword">let</span> t = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Brick</span>(&#123;
        <span class="hljs-attr">x</span>: item[<span class="hljs-number">0</span>],
        <span class="hljs-attr">y</span>: item[<span class="hljs-number">1</span>],
        <span class="hljs-attr">w</span>: <span class="hljs-number">60</span>,
        <span class="hljs-attr">h</span>: <span class="hljs-number">60</span>
    &#125;)
    s2.<span class="hljs-title function_">add</span>(t)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样第一关的全部砖块就完成了，原本第一关是有铁砖的，这里还没有实现，所以全部用土砖</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4aac051396a0446ebac688278e7d51f4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">实现我方基地</h3>
<p>接下来实现我方的老巢，这个东西不管是我方坦克还是敌方坦克，被击中就GG了，也很简单</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Heart</span>&#123;
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params">option</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> = option.<span class="hljs-property">x</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> = option.<span class="hljs-property">y</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span> = option.<span class="hljs-property">w</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span> = option.<span class="hljs-property">h</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">type</span> = <span class="hljs-string">"Heart"</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Image</span>()
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span>.<span class="hljs-property">src</span> = <span class="hljs-string">"./heart.png"</span>
    &#125;
    <span class="hljs-title function_">draw</span>(<span class="hljs-params">ctx</span>) &#123;
        ctx.<span class="hljs-title function_">drawImage</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span>);
    &#125;
    <span class="hljs-title function_">destroy</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">parent</span>.<span class="hljs-title function_">remove</span>(<span class="hljs-variable language_">this</span>)
        <span class="hljs-comment">// 心脏都被摧毁了，直接GG</span>
        <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">"Game Over"</span>)
    &#125;
&#125;

<span class="hljs-keyword">let</span> heart = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Heart</span>(&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-number">360</span>,
    <span class="hljs-attr">y</span>: <span class="hljs-number">720</span>, <span class="hljs-comment">// 老巢初始位置</span>
    <span class="hljs-attr">w</span>: <span class="hljs-number">60</span>,
    <span class="hljs-attr">h</span>: <span class="hljs-number">60</span>
&#125;)
s2.<span class="hljs-title function_">add</span>(heart)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f936dd97614434997b79a4ebd1d00b7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">实现双方坦克</h3>
<p>接下来实现敌我双方坦克,坦克我们用4张不同方向的图片，切换方向就换，敌我双方坦克的属性其实是一样的，不过双方交互逻辑不一样。我们再创建一个<code>EnemyTank</code>来表示敌方坦克，初始我们只有一种，后面会追加更厉害的种类，无非是跑的更快，子弹发射的更快，子弹的速度更快，抗打击的次数更多</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Tank</span> &#123;
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params">option</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> = option.<span class="hljs-property">x</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> = option.<span class="hljs-property">y</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span> = option.<span class="hljs-property">w</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span> = option.<span class="hljs-property">h</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">type</span> = <span class="hljs-string">"Tank"</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">direction</span> = <span class="hljs-string">"up"</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Image</span>();
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span>.<span class="hljs-property">src</span> = <span class="hljs-string">"./tankup.png"</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">parent</span> = <span class="hljs-literal">null</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span> = <span class="hljs-number">10</span>
    &#125;
    <span class="hljs-title function_">draw</span>(<span class="hljs-params">ctx</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span>.<span class="hljs-property">src</span> = <span class="hljs-string">`./tank<span class="hljs-subst">$&#123;<span class="hljs-variable language_">this</span>.direction&#125;</span>.png`</span>;
        ctx.<span class="hljs-title function_">drawImage</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span>);
    &#125;
    <span class="hljs-title function_">setDirection</span>(<span class="hljs-params">d</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">direction</span> = d;
    &#125;
    <span class="hljs-title function_">destroy</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">parent</span>.<span class="hljs-title function_">remove</span>(<span class="hljs-variable language_">this</span>)
    &#125;
&#125;

<span class="hljs-comment">// 初始化一个我方坦克（黄色）</span>
<span class="hljs-keyword">let</span> tank = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Tank</span>(&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-number">480</span>,
    <span class="hljs-attr">y</span>: <span class="hljs-number">720</span>,
    <span class="hljs-attr">w</span>: <span class="hljs-number">60</span>,
    <span class="hljs-attr">h</span>: <span class="hljs-number">60</span>
&#125;)
s2.<span class="hljs-title function_">add</span>(tank)

<span class="hljs-comment">// 初始化一个敌方坦克（绿色）</span>
<span class="hljs-keyword">let</span> etank = <span class="hljs-keyword">new</span> <span class="hljs-title class_">EnemyTank</span>(&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">y</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">w</span>: <span class="hljs-number">60</span>,
    <span class="hljs-attr">h</span>: <span class="hljs-number">60</span>
&#125;)
s2.<span class="hljs-title function_">add</span>(tanke)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e21d2b51ec94097bbf932e44fb79b77~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>到目前为止，初始的场景我们已经搭建好了，但是这个时候还没有交互逻辑，接下来我们实现子弹</p>
<h3 data-id="heading-5">子弹</h3>
<p>子弹其实是一个很单纯的类，简单来说初始化之后就从<code>起点</code>（坦克发射时候的位置）以一定的速度运动到<code>终点</code>（场景边缘），然后<code>销毁</code>。这里我们添加了4个方向的子弹</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 子弹，从起点位置到终点位置，中间做碰撞检测，碰撞了就销毁</span>
<span class="hljs-keyword">class</span> <span class="hljs-title class_">Bullet</span> &#123;
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params">option</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">sx</span> = option.<span class="hljs-property">sx</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">sy</span> = option.<span class="hljs-property">sy</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">ex</span> = option.<span class="hljs-property">ex</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">ey</span> = option.<span class="hljs-property">ey</span> <span class="hljs-comment">// 起点和终点</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> = <span class="hljs-variable language_">this</span>.<span class="hljs-property">sx</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> = <span class="hljs-variable language_">this</span>.<span class="hljs-property">sy</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span> = option.<span class="hljs-property">w</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span> = option.<span class="hljs-property">h</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">direction</span> = option.<span class="hljs-property">direction</span> <span class="hljs-comment">// 直接初始化传入即可，不再更新，子弹不拐弯</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">type</span> = <span class="hljs-string">"Bullet"</span>;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Image</span>();
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span>.<span class="hljs-property">src</span> = <span class="hljs-string">`./bullet<span class="hljs-subst">$&#123;<span class="hljs-variable language_">this</span>.direction&#125;</span>.png`</span>;

        <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span> = <span class="hljs-number">16</span>; <span class="hljs-comment">// 初始速度</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">level</span> = <span class="hljs-number">20</span>;

        <span class="hljs-comment">// 初始化就发射出去</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">fire</span>()
    &#125;
    <span class="hljs-title function_">draw</span>(<span class="hljs-params">ctx</span>) &#123;
        ctx.<span class="hljs-title function_">drawImage</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span>);
    &#125;
    <span class="hljs-title function_">destroy</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">parent</span>.<span class="hljs-title function_">remove</span>(<span class="hljs-variable language_">this</span>)
    &#125;
    <span class="hljs-title function_">fire</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">timer</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Timer</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 以符合子弹等级的速度运动完，这里其实一般只有x或者y变化，不会同时变的，那样就斜着飞了</span>
            <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> += (<span class="hljs-variable language_">this</span>.<span class="hljs-property">ex</span> - <span class="hljs-variable language_">this</span>.<span class="hljs-property">sx</span>) / <span class="hljs-variable language_">this</span>.<span class="hljs-property">level</span>
            <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> += (<span class="hljs-variable language_">this</span>.<span class="hljs-property">ey</span> - <span class="hljs-variable language_">this</span>.<span class="hljs-property">sy</span>) / <span class="hljs-variable language_">this</span>.<span class="hljs-property">level</span>
        &#125;, <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>)
    &#125;
&#125;
<span class="hljs-comment">// 初始化一颗子弹，后面由坦克触发</span>
<span class="hljs-keyword">let</span> b = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Bullet</span>(&#123;
    <span class="hljs-attr">sx</span>: <span class="hljs-number">360</span>,
    <span class="hljs-attr">sy</span>: <span class="hljs-number">720</span>, <span class="hljs-comment">// 坦克所在的位置</span>
    <span class="hljs-attr">ex</span>: <span class="hljs-number">360</span>,
    <span class="hljs-attr">ey</span>: -<span class="hljs-number">20</span>, <span class="hljs-comment">// x不变，运动到-20，直到看不见就销毁</span>
    <span class="hljs-attr">w</span>: <span class="hljs-number">10</span>,
    <span class="hljs-attr">h</span>: <span class="hljs-number">20</span>, <span class="hljs-comment">// 竖着的子弹尺寸</span>
    <span class="hljs-attr">direction</span>: <span class="hljs-string">"up"</span> <span class="hljs-comment">// 方向</span>
&#125;)
s2.<span class="hljs-title function_">add</span>(b)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa59e3e415ed404895a018b59e6f9988~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="zidan.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样子弹就实现了，在实现坦克发射子弹之前，我们来实现坦克的移动，设置方向，根据等级和速度移动即可</p>
<h3 data-id="heading-6">坦克移动</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Tank</span> &#123;
    <span class="hljs-comment">// 省略</span>
    <span class="hljs-title function_">setDirection</span>(<span class="hljs-params">d</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">direction</span> = d;
    &#125;
    <span class="hljs-title function_">move</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">switch</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">direction</span>) &#123;
            <span class="hljs-keyword">case</span> <span class="hljs-string">"up"</span>:
                <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> -= <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>;
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> <span class="hljs-string">"right"</span>:
                <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> += <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>;
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> <span class="hljs-string">"down"</span>:
                <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> += <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>;
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> <span class="hljs-string">"left"</span>:
                <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> -= <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>;
                <span class="hljs-keyword">break</span>;
        &#125;
    &#125;
&#125;
<span class="hljs-comment">// 给方向键添加上移动监听</span>
<span class="hljs-variable language_">document</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">"keyup"</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span>(e.<span class="hljs-property">code</span>) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ArrowUp"</span>: 
            tank.<span class="hljs-title function_">setDirection</span>(<span class="hljs-string">"up"</span>)
            tank.<span class="hljs-title function_">move</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ArrowRight"</span>: 
            tank.<span class="hljs-title function_">setDirection</span>(<span class="hljs-string">"right"</span>)
            tank.<span class="hljs-title function_">move</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ArrowDown"</span>: 
            tank.<span class="hljs-title function_">setDirection</span>(<span class="hljs-string">"down"</span>)
            tank.<span class="hljs-title function_">move</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ArrowLeft"</span>: 
            tank.<span class="hljs-title function_">setDirection</span>(<span class="hljs-string">"left"</span>)
            tank.<span class="hljs-title function_">move</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-attr">default</span>: 
            <span class="hljs-keyword">break</span>
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e00a2673f27844ac8b5c3ae65ae850e6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="move.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">坦克发射子弹</h3>
<p>坦克和子弹实现之后，给坦克加上<code>fire</code>事件，因为坦克和子弹都是有大小的，要让子弹看上去像是从枪管里发射出去的，结合<code>坦克当前位置</code>，<code>坦克方向</code>，<code>坦克大小</code>，<code>子弹大小</code>，<code>场景边缘</code>初始化一个子弹即可，子弹会执行自己的运动逻辑</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">document</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">"keyup"</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span>(e.<span class="hljs-property">code</span>) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"Space"</span>:
            tank.<span class="hljs-title function_">fire</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-attr">default</span>: 
            <span class="hljs-keyword">break</span>
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Tank</span> &#123;
    <span class="hljs-title function_">fire</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">let</span> opt = &#123;&#125;
        <span class="hljs-keyword">switch</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">direction</span>) &#123;
            <span class="hljs-keyword">case</span> <span class="hljs-string">"up"</span>:
                opt = &#123;
                    <span class="hljs-attr">sx</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span> / <span class="hljs-number">2</span> - config.<span class="hljs-property">bullet</span>.<span class="hljs-property">w</span> / <span class="hljs-number">2</span>,
                    <span class="hljs-attr">sy</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> - config.<span class="hljs-property">bullet</span>.<span class="hljs-property">h</span>,
                    <span class="hljs-attr">ex</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span> / <span class="hljs-number">2</span> - config.<span class="hljs-property">bullet</span>.<span class="hljs-property">w</span> / <span class="hljs-number">2</span>,
                    <span class="hljs-attr">ey</span>: -config.<span class="hljs-property">bullet</span>.<span class="hljs-property">h</span>,
                    <span class="hljs-attr">w</span>: config.<span class="hljs-property">bullet</span>.<span class="hljs-property">w</span>,
                    <span class="hljs-attr">h</span>: config.<span class="hljs-property">bullet</span>.<span class="hljs-property">h</span>,
                    <span class="hljs-attr">direction</span>: <span class="hljs-string">"up"</span>
                &#125;
                <span class="hljs-keyword">break</span>
            <span class="hljs-keyword">case</span> <span class="hljs-string">"right"</span>:
                opt = &#123;
                    <span class="hljs-attr">sx</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span>,
                    <span class="hljs-attr">sy</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span> / <span class="hljs-number">2</span> - config.<span class="hljs-property">bullet</span>.<span class="hljs-property">w</span> / <span class="hljs-number">2</span>,
                    <span class="hljs-attr">ex</span>: config.<span class="hljs-property">stage</span>.<span class="hljs-property">w</span> + config.<span class="hljs-property">bullet</span>.<span class="hljs-property">h</span>,
                    <span class="hljs-attr">ey</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span> / <span class="hljs-number">2</span> - config.<span class="hljs-property">bullet</span>.<span class="hljs-property">w</span> / <span class="hljs-number">2</span>,
                    <span class="hljs-attr">w</span>: config.<span class="hljs-property">bullet</span>.<span class="hljs-property">h</span>,
                    <span class="hljs-attr">h</span>: config.<span class="hljs-property">bullet</span>.<span class="hljs-property">w</span>,
                    <span class="hljs-attr">direction</span>: <span class="hljs-string">"right"</span>
                &#125;
                <span class="hljs-keyword">break</span>
            <span class="hljs-keyword">case</span> <span class="hljs-string">"down"</span>:
                opt = &#123;
                    <span class="hljs-attr">sx</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span> / <span class="hljs-number">2</span> - config.<span class="hljs-property">bullet</span>.<span class="hljs-property">w</span> / <span class="hljs-number">2</span>,
                    <span class="hljs-attr">sy</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span>, 
                    <span class="hljs-attr">ex</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">w</span> / <span class="hljs-number">2</span> - config.<span class="hljs-property">bullet</span>.<span class="hljs-property">w</span> / <span class="hljs-number">2</span>,
                    <span class="hljs-attr">ey</span>: config.<span class="hljs-property">stage</span>.<span class="hljs-property">h</span> + config.<span class="hljs-property">bullet</span>.<span class="hljs-property">h</span>,
                    <span class="hljs-attr">w</span>: config.<span class="hljs-property">bullet</span>.<span class="hljs-property">w</span>,
                    <span class="hljs-attr">h</span>: config.<span class="hljs-property">bullet</span>.<span class="hljs-property">h</span>,
                    <span class="hljs-attr">direction</span>: <span class="hljs-string">"down"</span>
                &#125;
                <span class="hljs-keyword">break</span>
            <span class="hljs-keyword">case</span> <span class="hljs-string">"left"</span>:
                opt = &#123;
                    <span class="hljs-attr">sx</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> - config.<span class="hljs-property">bullet</span>.<span class="hljs-property">h</span>,
                    <span class="hljs-attr">sy</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span> / <span class="hljs-number">2</span> - config.<span class="hljs-property">bullet</span>.<span class="hljs-property">w</span> / <span class="hljs-number">2</span>,
                    <span class="hljs-attr">ex</span>: -config.<span class="hljs-property">bullet</span>.<span class="hljs-property">h</span>,
                    <span class="hljs-attr">ey</span>: <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">h</span> / <span class="hljs-number">2</span> - config.<span class="hljs-property">bullet</span>.<span class="hljs-property">w</span> / <span class="hljs-number">2</span>,
                    <span class="hljs-attr">w</span>: config.<span class="hljs-property">bullet</span>.<span class="hljs-property">h</span>,
                    <span class="hljs-attr">h</span>: config.<span class="hljs-property">bullet</span>.<span class="hljs-property">w</span>,
                    <span class="hljs-attr">direction</span>: <span class="hljs-string">"left"</span>
                &#125;
                <span class="hljs-keyword">break</span>
            <span class="hljs-attr">default</span>: 
                <span class="hljs-keyword">break</span>
        &#125;
        <span class="hljs-keyword">let</span> b = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Bullet</span>(opt)
        s2.<span class="hljs-title function_">add</span>(b)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c698f0c19d9947f3800c7c1295102147~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="fire2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样一个到处横行霸道还能发射子弹的坦克就完成了，接下来我们实现坦克移动的碰撞检测</p>
<h3 data-id="heading-8">碰撞检测</h3>
<p>我们已经实现了<code>墙壁</code>（土砖），横行霸道的<code>我方坦克</code>，横行霸道的<code>敌方坦克</code>，<code>子弹</code>，但是他们在场景上各爬各的，要实现它们之间的交互逻辑</p>
<ul>
<li>坦克碰到墙壁和场景边缘不能继续移动</li>
<li>我方子弹打中敌方坦克</li>
<li>敌方子弹打中我方坦克</li>
<li>子弹打中墙壁</li>
</ul>
<p>就要检测他们之间是否碰撞到了，关于碰撞检测有很多种方式，先说结论，我们使用<code>分离轴检测</code>，这里可以简述一下分离轴检测的原理。</p>
<h3 data-id="heading-9">分离轴检测的几个原理</h3>
<ol>
<li>一个<code>凸多边形</code>的所有的内部点一定都在任意一条边的一侧（非常重要，很好理解）
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/875a8ab7918349b98d7586d2d6cb7577~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
<li>两个没重叠的凸多边形，一定存在一条轴线（这条轴有很多，只要找到一条就可以了），使得两个多边形分别在轴的两边（非常重要，很好理解）</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a8601b4f4b84b808182d8e789c36188~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>那么多的分离轴中，一定有一条是平行于某条边的（非常重要，看图理解），两个多边形中间有无数条分离轴，但是一定有一条<code>mn</code>是平行<code>AB</code>的</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f3a2b8fb780405493dbd77fffa62fe0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>计算两个多边形所有顶点在<code>AB法向量</code>上的投影，如果没有相交，就存在这样的分离轴，看图，<code>多边形1</code>的投影点<code>abcde</code>和<code>多边形2</code>的投影点<code>fghij</code>是不相交的，那么很显然，<code>ef</code>中间很容易找到一根线就把两个多边形隔开了</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86d4e9a1595644fdaf1ec73388dd0e76~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>对所有的边都做上述的检测，只要找到一条轴就说明2者没有发生一丁点的重叠，反之2者就重叠了</li>
</ol>
<p>这里贴一下分离轴的代码实现，有兴趣的可以研究，没兴趣的可以直接拿去用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 坐标系向量</span>
<span class="hljs-keyword">class</span> <span class="hljs-title class_">Vector</span> &#123;
    <span class="hljs-attr">x</span>: number;
    <span class="hljs-attr">y</span>: number;
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params">x, y</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> = x;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> = y;
    &#125;
    <span class="hljs-comment">// 获取向量的长度</span>
    <span class="hljs-title function_">getLength</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">sqrt</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">pow</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span>, <span class="hljs-number">2</span>) + <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">pow</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span>, <span class="hljs-number">2</span>));
    &#125;
    <span class="hljs-comment">// 向量相加</span>
    <span class="hljs-title function_">add</span>(<span class="hljs-params">v: Vector</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vector</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> + v.<span class="hljs-property">x</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> + v.<span class="hljs-property">y</span>);
    &#125;
    <span class="hljs-comment">// 向量相减</span>
    <span class="hljs-title function_">sub</span>(<span class="hljs-params">v: Vector</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vector</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> - v.<span class="hljs-property">x</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> - v.<span class="hljs-property">y</span>);
    &#125;
    <span class="hljs-comment">// 向量点积</span>
    <span class="hljs-title function_">dot</span>(<span class="hljs-params">v: Vector</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> * v.<span class="hljs-property">x</span> + <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> * v.<span class="hljs-property">y</span>;
    &#125;
    <span class="hljs-comment">// 返回法向量</span>
    <span class="hljs-title function_">perp</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vector</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span>, -<span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span>);
    &#125;
    <span class="hljs-comment">// 单位向量</span>
    <span class="hljs-title function_">unit</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">let</span> d = <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">getLength</span>();
        <span class="hljs-keyword">return</span> d ? <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vector</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> / d, <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> / d) : <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vector</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
    &#125;
&#125;

<span class="hljs-comment">// 投影</span>
<span class="hljs-keyword">class</span> <span class="hljs-title class_">Projection</span> &#123;
    <span class="hljs-attr">min</span>: number
    <span class="hljs-attr">max</span>: number
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params">min, max</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">min</span> = min
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">max</span> = max
    &#125;
    <span class="hljs-comment">// 2个投影是否重叠</span>
    <span class="hljs-title function_">overlaps</span>(<span class="hljs-params">p : Projection</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">max</span> > p.<span class="hljs-property">min</span> && <span class="hljs-variable language_">this</span>.<span class="hljs-property">min</span> < p.<span class="hljs-property">max</span>
    &#125;
&#125;

<span class="hljs-keyword">class</span> <span class="hljs-title class_">Polygon</span> &#123;
    <span class="hljs-attr">points</span>: any;
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params">points</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">points</span> = points
    &#125;
    <span class="hljs-title function_">draw</span>(<span class="hljs-params">ctx</span>) &#123;
        ctx.<span class="hljs-title function_">beginPath</span>();
        ctx.<span class="hljs-property">lineWidth</span> = <span class="hljs-number">1</span>;
        ctx.<span class="hljs-title function_">moveTo</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">points</span>[<span class="hljs-number">0</span>].<span class="hljs-property">x</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">points</span>[<span class="hljs-number">0</span>].<span class="hljs-property">y</span>);
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">points</span>.<span class="hljs-title function_">slice</span>(<span class="hljs-number">1</span>).<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
            ctx.<span class="hljs-title function_">lineTo</span>(item.<span class="hljs-property">x</span>, item.<span class="hljs-property">y</span>)
        &#125;)
        ctx.<span class="hljs-title function_">lineTo</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">points</span>[<span class="hljs-number">0</span>].<span class="hljs-property">x</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">points</span>[<span class="hljs-number">0</span>].<span class="hljs-property">y</span>)
        ctx.<span class="hljs-property">strokeStyle</span> = <span class="hljs-string">"red"</span>;
        ctx.<span class="hljs-title function_">stroke</span>();
        ctx.<span class="hljs-title function_">closePath</span>();
    &#125;
&#125;

<span class="hljs-comment">// 获取多个点的所有投影轴</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">getAxes</span>(<span class="hljs-params">points</span>) &#123;
    <span class="hljs-keyword">let</span> axes = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, j = points.<span class="hljs-property">length</span> - <span class="hljs-number">1</span>; i < j; i++) &#123;
        <span class="hljs-keyword">let</span> v1 = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vector</span>(points[i].<span class="hljs-property">x</span>, points[i].<span class="hljs-property">y</span>);
        <span class="hljs-keyword">let</span> v2 = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vector</span>(points[i + <span class="hljs-number">1</span>].<span class="hljs-property">x</span>, points[i + <span class="hljs-number">1</span>].<span class="hljs-property">y</span>);
        axes.<span class="hljs-title function_">push</span>(v1.<span class="hljs-title function_">sub</span>(v2).<span class="hljs-title function_">perp</span>().<span class="hljs-title function_">unit</span>());
    &#125;
    <span class="hljs-keyword">let</span> firstPoint = points[<span class="hljs-number">0</span>];
    <span class="hljs-keyword">let</span> lastPoint = points[points.<span class="hljs-property">length</span> - <span class="hljs-number">1</span>];
    <span class="hljs-keyword">let</span> v1 = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vector</span>(lastPoint.<span class="hljs-property">x</span>, lastPoint.<span class="hljs-property">y</span>);
    <span class="hljs-keyword">let</span> v2 = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vector</span>(firstPoint.<span class="hljs-property">x</span>, firstPoint.<span class="hljs-property">y</span>);
    axes.<span class="hljs-title function_">push</span>(v1.<span class="hljs-title function_">sub</span>(v2).<span class="hljs-title function_">perp</span>().<span class="hljs-title function_">unit</span>());
    <span class="hljs-keyword">return</span> axes;
&#125;

<span class="hljs-comment">// 获取投影轴上的投影，参数为投影轴向量</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">getProjection</span>(<span class="hljs-params">v: Vector, points</span>) &#123;
    <span class="hljs-keyword">let</span> min = <span class="hljs-title class_">Number</span>.<span class="hljs-property">MAX_SAFE_INTEGER</span>;
    <span class="hljs-keyword">let</span> max = <span class="hljs-title class_">Number</span>.<span class="hljs-property">MIN_SAFE_INTEGER</span>;
    points.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">point</span> =></span> &#123;
        <span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Vector</span>(point.<span class="hljs-property">x</span>, point.<span class="hljs-property">y</span>);
        <span class="hljs-keyword">let</span> dotProduct = p.<span class="hljs-title function_">dot</span>(v);
        min = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">min</span>(min, dotProduct);
        max = <span class="hljs-title class_">Math</span>.<span class="hljs-title function_">max</span>(max, dotProduct);
    &#125;)
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-title class_">Projection</span>(min, max);
&#125;

<span class="hljs-comment">// 判断两个凸多边形是否碰撞</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">isCollision</span>(<span class="hljs-params">poly, poly2</span>) &#123;
    <span class="hljs-keyword">let</span> axes1 = <span class="hljs-title function_">getAxes</span>(poly.<span class="hljs-property">points</span>);
    <span class="hljs-keyword">let</span> axes2 = <span class="hljs-title function_">getAxes</span>(poly2.<span class="hljs-property">points</span>);
    <span class="hljs-keyword">let</span> axes = [...axes1, ...axes2];

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> ax <span class="hljs-keyword">of</span> axes) &#123;
        <span class="hljs-keyword">let</span> p1 = <span class="hljs-title function_">getProjection</span>(ax, poly.<span class="hljs-property">points</span>);
        <span class="hljs-keyword">let</span> p2 = <span class="hljs-title function_">getProjection</span>(ax, poly2.<span class="hljs-property">points</span>);
        <span class="hljs-keyword">if</span> (!p1.<span class="hljs-title function_">overlaps</span>(p2)) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们会得到一个函数，传入2个多边形的顶点数组（因为我们的元素都是由<code>xywh</code>描述的），返回他们是否碰撞</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">function</span> <span class="hljs-title function_">isCollision</span>(<span class="hljs-params">poly, poly2</span>) &#123;
    <span class="hljs-keyword">let</span> axes1 = <span class="hljs-title function_">getAxes</span>(poly.<span class="hljs-property">points</span>);
    <span class="hljs-keyword">let</span> axes2 = <span class="hljs-title function_">getAxes</span>(poly2.<span class="hljs-property">points</span>);
    <span class="hljs-keyword">let</span> axes = [...axes1, ...axes2];

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> ax <span class="hljs-keyword">of</span> axes) &#123;
        <span class="hljs-keyword">let</span> p1 = <span class="hljs-title function_">getProjection</span>(ax, poly.<span class="hljs-property">points</span>);
        <span class="hljs-keyword">let</span> p2 = <span class="hljs-title function_">getProjection</span>(ax, poly2.<span class="hljs-property">points</span>);
        <span class="hljs-keyword">if</span> (!p1.<span class="hljs-title function_">overlaps</span>(p2)) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">坦克，子弹，墙砖的碰撞</h3>
<p>由于坦克，子弹，墙砖都是长方形，也属于凸多边形的一种，而且顶点还特别少，可以直接套用</p>
<ul>
<li>在子弹的移动过程中，进行子弹和土砖、坦克的检测，如果碰撞了，就销毁子弹，土砖，和坦克</li>
<li>在坦克的移动过程中，进行坦克和土砖、坦克的检测，如果碰撞了，停止移动</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Bullet</span> &#123;
    <span class="hljs-title function_">fire</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-title function_">isCollision</span>(<span class="hljs-variable language_">this</span>, brick)) &#123;
            <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">destroy</span>()
            brick.<span class="hljs-title function_">destroy</span>()
        &#125;
        <span class="hljs-keyword">if</span>(<span class="hljs-title function_">isCollision</span>(<span class="hljs-variable language_">this</span>, tank)) &#123;
            <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">destroy</span>()
            tank.<span class="hljs-title function_">destroy</span>()
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>考虑到后续的扩展（坦克种类的增加，墙砖种类的增加，还有道具等），封装一个按照种类批量碰撞检测的函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// elms，所有的元素</span>
<span class="hljs-comment">// elm，当前检测碰撞元素</span>
<span class="hljs-comment">// type[]，要与之检测的元素种类</span>
<span class="hljs-comment">// cb，碰撞回调</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">checkCollision</span>(<span class="hljs-params">elms, elm, type, cb</span>) &#123;
    <span class="hljs-keyword">let</span> checkElms = elms.<span class="hljs-title function_">filter</span>(<span class="hljs-function"><span class="hljs-params">item</span> =></span> type.<span class="hljs-title function_">includes</span>(item.<span class="hljs-property">type</span>) && item.<span class="hljs-property">id</span> != elm.<span class="hljs-property">id</span>)
    <span class="hljs-keyword">let</span> p = <span class="hljs-literal">false</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;i < checkElms.<span class="hljs-property">length</span>;i++) &#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-title function_">isCollision</span>(<span class="hljs-title function_">getElementPoints</span>(checkElms[i]), <span class="hljs-title function_">getElementPoints</span>(elm))) &#123;
            p = <span class="hljs-literal">true</span>
            <span class="hljs-title function_">cb</span>(checkElms[i])
            <span class="hljs-keyword">break</span>
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> p
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样坦克的碰撞可以写成这样，以向上移动为例，可以把碰撞种类提取为配置，这样方便扩展</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">case</span> <span class="hljs-string">"left"</span>:
    <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> >= <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> -= <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>;
    &#125;
    elms = <span class="hljs-title function_">flatArrayChildren</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">parent</span>.<span class="hljs-property">children</span>);
    <span class="hljs-comment">// 我方坦克与墙和敌方普通坦克的碰撞检测，如果发生碰撞了，就把移动重置掉</span>
    <span class="hljs-title function_">checkCollision</span>(elms, <span class="hljs-variable language_">this</span>, [<span class="hljs-string">"Brick"</span>, <span class="hljs-string">"EnemyTank"</span>], <span class="hljs-function">(<span class="hljs-params">elm</span>) =></span> &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> += <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>
    &#125;)
    <span class="hljs-keyword">break</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候一个完整机制的游戏已经完成了，初始化一个我方坦克，控制移动和发射子弹，子弹会自动检测摧毁目标，按一定的机制初始化敌方坦克，随机发射子弹。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 初始化舞台</span>
<span class="hljs-keyword">let</span> s2 = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Stage</span>(<span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"stage"</span>));

<span class="hljs-comment">// 初始化所有的墙砖</span>
<span class="hljs-keyword">let</span> tuzhuans = shut.<span class="hljs-property">one</span>
tuzhuans.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-keyword">let</span> t = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Brick</span>(&#123;
        <span class="hljs-attr">x</span>: item[<span class="hljs-number">0</span>],
        <span class="hljs-attr">y</span>: item[<span class="hljs-number">1</span>],
        <span class="hljs-attr">w</span>: <span class="hljs-number">60</span>,
        <span class="hljs-attr">h</span>: <span class="hljs-number">60</span>
    &#125;)
    s2.<span class="hljs-title function_">add</span>(t)
&#125;)
<span class="hljs-comment">// 初始化一个我方老巢</span>
<span class="hljs-keyword">let</span> heart = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Heart</span>(&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-number">360</span>,
    <span class="hljs-attr">y</span>: <span class="hljs-number">720</span>,
    <span class="hljs-attr">w</span>: <span class="hljs-number">60</span>,
    <span class="hljs-attr">h</span>: <span class="hljs-number">60</span>
&#125;)
s2.<span class="hljs-title function_">add</span>(heart)

<span class="hljs-comment">// 初始化一个我方坦克</span>
<span class="hljs-keyword">let</span> tank = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Tank</span>(&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-number">480</span>,
    <span class="hljs-attr">y</span>: <span class="hljs-number">720</span>,
    <span class="hljs-attr">w</span>: <span class="hljs-number">60</span>,
    <span class="hljs-attr">h</span>: <span class="hljs-number">60</span>
&#125;)
s2.<span class="hljs-title function_">add</span>(tank)

<span class="hljs-comment">// 初始化一个敌方坦克</span>
<span class="hljs-keyword">let</span> etank = <span class="hljs-keyword">new</span> <span class="hljs-title class_">EnemyTank</span>(&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-number">480</span>,
    <span class="hljs-attr">y</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">w</span>: <span class="hljs-number">60</span>,
    <span class="hljs-attr">h</span>: <span class="hljs-number">60</span>
&#125;)
s2.<span class="hljs-title function_">add</span>(etank)

<span class="hljs-comment">// 我方坦克控制交互</span>
<span class="hljs-variable language_">document</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">"keyup"</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span>(e.<span class="hljs-property">code</span>) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ArrowUp"</span>: 
            tank.<span class="hljs-title function_">setDirection</span>(<span class="hljs-string">"up"</span>)
            tank.<span class="hljs-title function_">move</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ArrowRight"</span>: 
            tank.<span class="hljs-title function_">setDirection</span>(<span class="hljs-string">"right"</span>)
            tank.<span class="hljs-title function_">move</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ArrowDown"</span>: 
            tank.<span class="hljs-title function_">setDirection</span>(<span class="hljs-string">"down"</span>)
            tank.<span class="hljs-title function_">move</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ArrowLeft"</span>: 
            tank.<span class="hljs-title function_">setDirection</span>(<span class="hljs-string">"left"</span>)
            tank.<span class="hljs-title function_">move</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">"Space"</span>:
            tank.<span class="hljs-title function_">fire</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-attr">default</span>: 
            <span class="hljs-keyword">break</span>
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f6e5224b3c44c6689246bca7fe88128~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="fire3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>相信我，我已经很用力的在按方向键了，碰到墙砖是真的前进不了的，先来一发自杀，可以看到，碰撞检测是非常精准的，精度可以达到<code>1px</code>以内，子弹在碰到目标元素的一瞬间就触发了。</p>
<p>击毁敌方坦克
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4a82283ebf34c66b7542c9511a9e8f4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="fire4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们可以开始着手实现游戏机制了</p>
<ol>
<li>敌方势力强大，有很多坦克</li>
<li>敌方的驾驶员是猪，上一颗子弹销毁了才会发射下一颗，每0.5s才会进行一次移动</li>
<li>我方坦克过于老旧，上一颗子弹销毁了才会发射下一颗</li>
<li>敌方驾驶员喝大酒了，一直前进，直到碰到墙或者坦克，才会随机进行一次转向</li>
</ol>
<p>敌方坦克AI</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">EnemyTank</span> &#123;
    <span class="hljs-title function_">action</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">actionTimer</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Timer</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">fire</span>()
        &#125;, <span class="hljs-number">500</span>)
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">moveTimer</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Timer</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">move</span>()
        &#125;, <span class="hljs-number">500</span>)
    &#125;,
    <span class="hljs-title function_">randomDirection</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">setDirection</span>([<span class="hljs-string">'up'</span>, <span class="hljs-string">'down'</span>, <span class="hljs-string">'right'</span>, <span class="hljs-string">'left'</span>][<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">floor</span>(<span class="hljs-title class_">Math</span>.<span class="hljs-title function_">random</span>() * <span class="hljs-number">4</span>)])
    &#125;
    <span class="hljs-title function_">move</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-keyword">switch</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">direction</span>) &#123;
            <span class="hljs-keyword">case</span> <span class="hljs-string">"up"</span>:
                <span class="hljs-keyword">if</span> (<span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> >= <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>) &#123;
                    <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> -= <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>;
                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-comment">// 碰到边缘了也随机换方向</span>
                    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">randomDirection</span>()
                &#125;
                elms = <span class="hljs-title function_">flatArrayChildren</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">parent</span>.<span class="hljs-property">children</span>);
                <span class="hljs-title function_">checkCollision</span>(elms, <span class="hljs-variable language_">this</span>, [<span class="hljs-string">"Brick"</span>, <span class="hljs-string">"Tank"</span>, <span class="hljs-string">"EnemyTank"</span>], <span class="hljs-function">(<span class="hljs-params">elm</span>) =></span> &#123;
                    <span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> += <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>
                    <span class="hljs-comment">// 碰到墙了就随机换方向</span>
                    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">randomDirection</span>()
                &#125;)
                <span class="hljs-keyword">break</span>;
        <span class="hljs-comment">// 省略</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>做完这些，就可以初始化游戏了</p>
<ol>
<li>初始化舞台</li>
<li>初始化墙砖</li>
<li>初始化我方坦克，方向键移动，空格键发射</li>
<li>初始化敌方坦克们</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> s2 = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Stage</span>(<span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"stage"</span>));
<span class="hljs-keyword">let</span> tuzhuans = shut.<span class="hljs-property">one</span>
tuzhuans.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-keyword">let</span> t = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Brick</span>(&#123;
        <span class="hljs-attr">x</span>: item[<span class="hljs-number">0</span>],
        <span class="hljs-attr">y</span>: item[<span class="hljs-number">1</span>],
        <span class="hljs-attr">w</span>: <span class="hljs-number">60</span>,
        <span class="hljs-attr">h</span>: <span class="hljs-number">60</span>
    &#125;)
    s2.<span class="hljs-title function_">add</span>(t)
&#125;)
<span class="hljs-keyword">let</span> heart = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Heart</span>(&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-number">360</span>,
    <span class="hljs-attr">y</span>: <span class="hljs-number">720</span>,
    <span class="hljs-attr">w</span>: <span class="hljs-number">60</span>,
    <span class="hljs-attr">h</span>: <span class="hljs-number">60</span>
&#125;)
s2.<span class="hljs-title function_">add</span>(heart)

<span class="hljs-keyword">let</span> tank = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Tank</span>(&#123;
    <span class="hljs-attr">x</span>: <span class="hljs-number">480</span>,
    <span class="hljs-attr">y</span>: <span class="hljs-number">720</span>,
    <span class="hljs-attr">w</span>: <span class="hljs-number">60</span>,
    <span class="hljs-attr">h</span>: <span class="hljs-number">60</span>
&#125;)
s2.<span class="hljs-title function_">add</span>(tank)

<span class="hljs-keyword">let</span> enemyTanks = [[<span class="hljs-number">60</span>, <span class="hljs-number">0</span>], [<span class="hljs-number">180</span>, <span class="hljs-number">0</span>], [<span class="hljs-number">300</span>, <span class="hljs-number">0</span>], [<span class="hljs-number">420</span>, <span class="hljs-number">0</span>], [<span class="hljs-number">540</span>, <span class="hljs-number">0</span>], [<span class="hljs-number">660</span>, <span class="hljs-number">0</span>],
                  [<span class="hljs-number">180</span>, <span class="hljs-number">420</span>], [<span class="hljs-number">540</span>, <span class="hljs-number">420</span>]]
enemyTanks.<span class="hljs-title function_">forEach</span>(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-keyword">let</span> t = <span class="hljs-keyword">new</span> <span class="hljs-title class_">EnemyTank</span>(&#123;
        <span class="hljs-attr">x</span>: item[<span class="hljs-number">0</span>],
        <span class="hljs-attr">y</span>: item[<span class="hljs-number">1</span>],
        <span class="hljs-attr">w</span>: <span class="hljs-number">60</span>,
        <span class="hljs-attr">h</span>: <span class="hljs-number">60</span>
    &#125;)
    t.<span class="hljs-title function_">action</span>()
    s2.<span class="hljs-title function_">add</span>(t)
&#125;)

<span class="hljs-variable language_">document</span>.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">"keyup"</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-keyword">switch</span>(e.<span class="hljs-property">code</span>) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ArrowUp"</span>: 
            tank.<span class="hljs-title function_">setDirection</span>(<span class="hljs-string">"up"</span>)
            tank.<span class="hljs-title function_">move</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ArrowRight"</span>: 
            tank.<span class="hljs-title function_">setDirection</span>(<span class="hljs-string">"right"</span>)
            tank.<span class="hljs-title function_">move</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ArrowDown"</span>: 
            tank.<span class="hljs-title function_">setDirection</span>(<span class="hljs-string">"down"</span>)
            tank.<span class="hljs-title function_">move</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">"ArrowLeft"</span>: 
            tank.<span class="hljs-title function_">setDirection</span>(<span class="hljs-string">"left"</span>)
            tank.<span class="hljs-title function_">move</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">"Space"</span>:
            tank.<span class="hljs-title function_">fire</span>()
            <span class="hljs-keyword">break</span>
        <span class="hljs-attr">default</span>: 
            <span class="hljs-keyword">break</span>
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先来体验一把，看我神威，无坚不摧
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0d2dca29d7144429bc1e5879ada8dc6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="game.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>竟然没打过，可惜，再来一把
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54b9cfa175bc4810a8e3d52eea5d99e2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="game2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>又没打过，可恶，再来，把坦克的初始方向改成向左，这样他们就不会开始就向下进攻了，总算打过了
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a55e755d32f84748aab9086420533f48~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="game3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">其他类型的砖块</h3>
<p>虽然游戏的基本功能已经完成了，但是我们只有一种土砖，实际还有其他功能的砖块的</p>
<ul>
<li>土砖，阻挡坦克移动，任意子弹都能击毁</li>
<li>铁砖，阻挡坦克移动，普通子弹不能击毁，吃到三颗星星以上的坦克发射的子弹可以击毁</li>
<li>水砖，阻挡坦克移动，子弹可以穿过，不能销毁</li>
<li>草砖，坦克可以移动，但是会遮盖坦克，特殊子弹可以击毁</li>
</ul>
<h3 data-id="heading-12">实现铁砖和水砖</h3>
<p>由于我们已经实现了土砖，所以这里只需要继承一下，设置一下类型即可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">SteelBrick</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">Brick</span> &#123;
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params">option</span>) &#123;
        <span class="hljs-variable language_">super</span>(option)
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">type</span> = <span class="hljs-string">"SteelBrick"</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Image</span>()
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span>.<span class="hljs-property">src</span> = <span class="hljs-string">"./tiezhuan.png"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">WaterBrick</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_ inherited__">Brick</span> &#123;
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params">option</span>) &#123;
        <span class="hljs-variable language_">super</span>(option)
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">type</span> = <span class="hljs-string">"WaterBrick"</span>
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Image</span>()
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">image</span>.<span class="hljs-property">src</span> = <span class="hljs-string">"./shuizhuan.png"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">新的碰撞</h3>
<p>由于铁砖和水砖的碰撞逻辑是特殊的，那我们是不是又要重新写之前的碰撞逻辑呢？</p>
<p>答案是不需要，因为我们前面已经把碰撞的逻辑封装成按类型去检测了，所以砖块的检测逻辑就成了这样</p>
<ul>
<li>土砖，与所有的子弹进行碰撞检测，碰撞后销毁子弹和土砖</li>
<li>铁砖，与所有的子弹进行碰撞检测，普通子弹销毁，特殊子弹同时销毁铁砖</li>
<li>水砖，只与坦克进行碰撞检测，阻止移动</li>
<li>草砖，只与特殊子弹进行碰撞检测，同时销毁子弹和草砖</li>
</ul>
<p>我们稍微改一下子弹和坦克的碰撞逻辑</p>
<p>在子弹的逻辑中，把铁砖加进要检测的类型里，然后不销毁就可以了，水砖根本不用与子弹检测</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Bullet</span> &#123;
    <span class="hljs-comment">// 省略</span>
    <span class="hljs-title function_">fire</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-comment">// 省略</span>
        <span class="hljs-comment">// 把 SteelBrick 加入要检测的类型数组里</span>
        <span class="hljs-title function_">checkCollision</span>(elms, <span class="hljs-variable language_">this</span>, [<span class="hljs-string">"SteelBrick"</span>, <span class="hljs-string">"Brick"</span>, <span class="hljs-string">"EnemyTank"</span>, <span class="hljs-string">"Heart"</span>], <span class="hljs-function">(<span class="hljs-params">elm</span>) =></span> &#123;
            <span class="hljs-keyword">if</span>(elm.<span class="hljs-property">type</span> != <span class="hljs-string">"SteelBrick"</span>) &#123;
                elm.<span class="hljs-title function_">destroy</span>()
            &#125;
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在坦克的移动碰撞检测里，加上铁砖即可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Tank</span> &#123;
    <span class="hljs-title function_">move</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-comment">// 省略</span>
        <span class="hljs-title function_">checkCollision</span>(elms, <span class="hljs-variable language_">this</span>, [<span class="hljs-string">"SteelBrick"</span>, <span class="hljs-string">"Brick"</span>, <span class="hljs-string">"EnemyTank"</span>])
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们特殊的砖块就加入到游戏中了，从上面的实现可以看到，砖块的扩展是很方便的，以后有什么金砖银砖要加进游戏也很简单</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ecc151b672344079beee39e380e2a8c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="steel.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d2e008e7e534ada816fcb896c08c3bd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="water.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">高级坦克</h3>
<p>高级砖块有了，那么高级坦克自然也要有，主要是敌方坦克，我方坦克是吃道具升级的（说到这里，后面肯定要实现道具了）</p>
<ul>
<li>道具坦克，因为游戏中该坦克总是闪烁着红光，我喜欢叫它红坦克，击毁后会在地图上掉落随机道具，可能与墙砖重叠</li>
<li>高级坦克，主要是跑的更快，子弹速度更快，抗揍，打中几次才会击毁</li>
</ul>
<h3 data-id="heading-15">抗揍能力</h3>
<p>上面提到，高级坦克是能抗好几发子弹的，那这个逻辑怎么顺利的加到我们的游戏里呢？一开始我的想法是在碰撞里做检测，判断坦克的类型，达到次数后再销毁</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title function_">checkCollision</span>(elms, <span class="hljs-variable language_">this</span>, [<span class="hljs-string">"SeniorEnemyTank"</span>], <span class="hljs-function">(<span class="hljs-params">elm</span>) =></span> &#123;
    <span class="hljs-comment">// 每中一次弹就减一次，直到销毁</span>
    <span class="hljs-keyword">if</span>(elm.<span class="hljs-property">lifeCount</span> > <span class="hljs-number">0</span>) &#123;
        elm.<span class="hljs-property">lifeCount</span> --
    &#125; <span class="hljs-keyword">else</span> &#123;
        elm.<span class="hljs-title function_">destroy</span>()
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这样等坦克种类多的时候，里面的逻辑就很混乱，于是我把子弹碰撞的逻辑改成了<code>中弹</code>，不管是坦克还是墙砖，只要与子弹碰撞了就调用中弹，至于中弹之后是该销毁还是减少血量，各元素内部自行处理，包括上面提到的安全帽道具，我方坦克还是会中弹，但是中弹之后，由于自身有安全帽，那么不执行中弹的后果就行了，这样逻辑就清晰很多</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title function_">checkCollision</span>(elms, <span class="hljs-variable language_">this</span>, [<span class="hljs-string">"SeniorEnemyTank"</span>], <span class="hljs-function">(<span class="hljs-params">elm</span>) =></span> &#123;
    <span class="hljs-comment">// 元素中弹</span>
    elm.<span class="hljs-title function_">gotShot</span>()
    <span class="hljs-comment">// 子弹自己销毁</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">destroy</span>()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>高级坦克的中弹处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">SeniorEnemyTank</span> &#123;
    <span class="hljs-title function_">constructor</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">lifeCount</span> = <span class="hljs-number">4</span>
    &#125;
    <span class="hljs-title function_">gotShot</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">lifeCount</span> --
        <span class="hljs-keyword">if</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">lifeCount</span> <= <span class="hljs-number">0</span>) &#123;
            <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">destroy</span>()
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a846d8d8a64642a5b3b8ec64221c3217~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="senior.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，普通坦克（绿色）一发子弹就挂了，高级坦克（白色）要打中4次才会挂掉，更多高级的坦克只是属性不同罢了，这里就不多搞了</p>
<h3 data-id="heading-16">铁砖的优化</h3>
<p>还记得前面铁砖的逻辑吗，我们在子弹的逻辑里是这样写的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title function_">checkCollision</span>(elms, <span class="hljs-variable language_">this</span>, [<span class="hljs-string">"SteelBrick"</span>], <span class="hljs-function">(<span class="hljs-params">elm</span>) =></span> &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">destroy</span>()
    <span class="hljs-keyword">if</span>(elm.<span class="hljs-property">type</span> != <span class="hljs-string">"SteelBrick"</span>) &#123;
        elm.<span class="hljs-title function_">destroy</span>()
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在也可以把中弹的逻辑优化上去了，铁砖中弹无事即可</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title function_">checkCollision</span>(elms, <span class="hljs-variable language_">this</span>, [<span class="hljs-string">"SteelBrick"</span>], <span class="hljs-function">(<span class="hljs-params">elm</span>) =></span> &#123;
    elm.<span class="hljs-title function_">gotShot</span>()
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">destroy</span>()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">SteelBrick</span> &#123;
    <span class="hljs-title function_">gotShot</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-comment">// do nothing</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">道具来了</h3>
<p>一个游戏没有道具那还玩个锤子，前面我们已经实现了抗揍的高级敌方坦克，现在要实现给我们送道具的红坦克，击毁后会在地图随机一个位置生成一个随机道具，道具的功能各种各样，有些道具比较简单，就不一一实现了，说一下实现原理就行了</p>
<ul>
<li>坦克，吃了加一条命，不做，要实现的话，搞个全局变量记个数就行了，我方坦克挂了，在初始位置再弄一个</li>
<li>时钟，吃了敌方坦克定身一定时间，不做，要实现的话，在所有敌方坦克的控制逻辑里加上变量校验就行了</li>
<li>铁锹，吃了我方城堡外面的砖一定时间内变成铁砖，不做，要实现的话，搞个定时器把对应位置的砖换一下就行了</li>
<li>安全帽，吃了我方坦克无敌，不做，要做的话也是一样，搞个变量，在我方坦克中弹的时候判断一下就行了</li>
<li>炸弹，吃了所有敌方坦克全部爆炸，不做，这个太简单了</li>
<li><code>星星，吃了我方坦克可以加速，子弹速度变快，3个以上可以打铁砖，这个要做一下，坦克就靠这个升级了</code></li>
</ul>
<h3 data-id="heading-18">星星道具效果</h3>
<ul>
<li>加速，吃了坦克移速更快，子弹速度也更快</li>
<li>加攻击，吃了坦克的子弹攻击力更大，原本打几下才能死的坦克可以一下打死</li>
<li>质变，我记得好像3颗星星之后，子弹就可以打铁砖了，这里就不搞这么花里胡哨了</li>
<li>抗揍，有的版本里好像吃多了星星还能抗子弹，这里就不搞这么花里胡哨了</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Star</span> &#123;
    <span class="hljs-comment">// 省略</span>
    <span class="hljs-title function_">beEaten</span>(<span class="hljs-params">elm</span>) &#123;
        <span class="hljs-comment">// 星星被吃之后，给目标加属性，其他道具一样的逻辑</span>
        <span class="hljs-comment">// 比如炸弹，在这里直接销毁所有敌方坦克就完事了</span>
        elm.<span class="hljs-property">star</span> ++
        <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">destroy</span>()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">坦克加速</h3>
<p>坦克增加<code>星星数</code>、<code>速度</code>、<code>攻击力</code>的属性，吃到星星的时候改变属性，然后坦克的交互加上这些属性的计算</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">this</span>.<span class="hljs-property">x</span> += <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>
<span class="hljs-comment">// 或者</span>
<span class="hljs-variable language_">this</span>.<span class="hljs-property">y</span> += <span class="hljs-variable language_">this</span>.<span class="hljs-property">speed</span>
<span class="hljs-comment">// 子弹的话，初始化的时候传递一个更大的参数即可</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">坦克加攻击</h3>
<p>前面我们实现了坦克或者墙砖的中弹逻辑，现在加上子弹攻击力的逻辑，默认子弹的杀伤力是<code>1</code>，吃了星星之后就<code>加1</code>，在中弹的时候传递给对应的中弹目标，进行扣血逻辑</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 由于子弹的参数是完全由坦克的状态初始化的，星星越多的坦克，初始化出来的子弹伤害越高，</span>
<span class="hljs-title function_">checkCollision</span>(elms, <span class="hljs-variable language_">this</span>, [<span class="hljs-string">"Brick"</span>, <span class="hljs-string">"EnemyTank"</span>], <span class="hljs-function">(<span class="hljs-params">elm</span>) =></span> &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">destroy</span>()
    elm.<span class="hljs-title function_">gotShot</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">hurt</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相应的，坦克中弹逻辑就要加上伤害的处理了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Tank</span> &#123;
    <span class="hljs-comment">// 反正减到0以下就挂了</span>
    <span class="hljs-title function_">gotShot</span>(<span class="hljs-params">hurt</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">lifeCount</span> -= hurt
        <span class="hljs-keyword">if</span>(<span class="hljs-variable language_">this</span>.<span class="hljs-property">lifeCount</span> <= <span class="hljs-number">0</span>) &#123;
            <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">destroy</span>()
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>坦克里加上与道具的碰撞去吃掉，同时增加属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">class</span> <span class="hljs-title class_">Tank</span> &#123;
    <span class="hljs-title function_">move</span>(<span class="hljs-params"></span>) &#123;
        <span class="hljs-comment">// 单独加上吃道具逻辑，后续可以扩展</span>
        <span class="hljs-title function_">checkCollision</span>(elms, <span class="hljs-variable language_">this</span>, [<span class="hljs-string">"Star"</span>], <span class="hljs-function">(<span class="hljs-params">elm</span>) =></span> &#123;
            elm.<span class="hljs-title function_">beEaten</span>(<span class="hljs-variable language_">this</span>)
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看下图，原本一辆高级坦克我们要攻击4下才可以打死，因为我们默认攻击力为1，但是我们吃了一颗星星后，只需要攻击2次就打死了
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca6da83f3d2f4c37b1c598cabc6dc1e9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="star.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">优化</h3>
<p>其实游戏机制到这里已经差不多了（还剩一些简单的交互），剩下的无非是怎么合理的设计每局的墙砖类型和分布，怎么增加敌方的坦克，或者优化敌方坦克的移动和发射机制（这个需要专业的人去设计了），或者扩展我方坦克的数量，地方坦克的种类，道具的种类等等，这都不是我们要考虑的了，但是从代码层面来说，还是有要优化提升的地方。</p>
<ol>
<li>碰撞检测的优化</li>
</ol>
<p>现在是按照类型去做检测，例如每颗子弹都会与所有的砖块检测，每个坦克也会与所有的砖块检测，地图上每<code>2个元素</code>之间就要做一次碰撞检测，而每一次检测又要对所有的顶点做投影计算，这样的检测每隔<code>16ms</code>一直不停的进行，非常的消耗性能。</p>
<p>很显然，基于我们朴素的观察，一颗左下角的子弹，是不可能与右上角的坦克碰撞的，基于这个朴素的认知，加上游戏里最大单位是<code>60px</code>，我们每次做碰撞检测的时候，只需要筛选出待检元素附近<code>60px</code>范围类的元素来检测就行了</p>
<ol start="2">
<li>代码的优化</li>
</ol>
<p>显然不管是敌方的坦克还是我方的坦克，大部分的逻辑都是一样的，所以有必要做一下封装。然后各个类自行去处理自己的逻辑</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 坦克继承</span>
xxTank <span class="hljs-keyword">extends</span> <span class="hljs-title class_">Tank</span>

<span class="hljs-comment">// 砖块继承 </span>
xxBrick <span class="hljs-keyword">extends</span> <span class="hljs-title class_">Brick</span>

<span class="hljs-comment">// 子弹继承</span>
xxBullet <span class="hljs-keyword">extends</span> <span class="hljs-title class_">Bullet</span>

<span class="hljs-comment">// 道具继承</span>
xxProp <span class="hljs-keyword">extends</span> <span class="hljs-title class_">Prop</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>配置的优化</li>
</ol>
<p>可以把很多值提取为配置，例如关卡砖块的分布，坦克的种类，子弹的种类，道具的种类，每种元素要与之做碰撞检测的元素，这样不管是扩展还是修改游戏机制，都会方便很多</p>
<h3 data-id="heading-22">结语</h3>
<p>到此为止，这款童年经典就算复刻完成了，有很多瑕疵，但是主要的游戏机制都有了，那些交互逻辑，敌方坦克的AI，关卡分布的逻辑，就不再往下还原了，有兴趣的可以把相关内容私信给我，有空加进去。</p></div>  
</div>
            