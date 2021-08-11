
---
title: 'OC底层原理（九）：objc_msgSend消息的慢速查找分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=9800'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 04:12:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=9800'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAdCAYAAABcz8ldAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAhgSURBVGhD7Zp7bBTHHcdn33t7vvOdzy+ITVKDU0xIKG2ABCPTRCCaUiEVKWoqRJuASAhCitRCVKSoalFUKZBiSmmFRRJKRUnUtIpo+aNqGgwoOCmuFUIRzxjwE4zte+97drYzztji8HPvtkit/PnH+n1397Tz+83vN/PbMZhmmmmm+d+BoX8n5diihcGqgFQf5vk6BMAskWUlw3GyFnIvtqWSf91w7mKC3npfOLX7wYeiIa6BBWCOLLFRF2NB0JvIOP/80YG+k2ev6S699b/OzOfKBW5l5KsgyC4DCFQDnpEAdE1goc/dlNPc/Up7P711UiYNSMuyxeUzZPnHgGHWh5XADEkSAcdiN+AnEXIBhBComgFU0/xQR+jnj51sOUMf9Z0NKyL8S9+JPBEN8zuCMrsqGOA5QWAAyzLAxe53HBeYFgJp1c5Cx33nyIfpV3e+22/Sx32nev/sMCgVnmM4bjOniAtZWQAsz315EfsGQQc4hgWcjHkCmOj1rheuNn95cXwmDMiVp5etC/D8m5FwUWVQUYYGPh6mZYFUOgsGVa1pXvOZzVT2jRuH54RM230jEuI3RcIiL4l4UkxAJmuD/riVsqD7ct2m9nep7BtVTbVfZ0uE/UIk+CQflAHDjf8+Lg6MldYATGpH3c/Ul7p3dWXppVGM6eElJSHmnQWPbSlRlN1lJcUBjqNRnwJZVQO3B5P/uq5rK1d90pakckFcaKp5UJHY92JR8YlwkUDVySEZfGfQdO7E7Z8s2HL9TSoXTPXRud9nA8IBqSwcZgWeqpPj6BYw7yTbXBN9q2v9lQEq5zBmWA8vWLCptCi4tzwW8RQMQlFQATPLSh6vCSh/plJBkMyQBHZfWYnkKRgEktEVpTJXERN2Xzo4ex2VC6K6qXYpF5b3ypVRT8EgcAERSJXRbwCBOTFzXblM5RxGBaRt+ZPYA+LO0mgxz5K1Ig+UgAzKIuGnz39z6S+olDeaibaXRsU1RUFvgx+GwTWgPCaDgMw2XXpr9gwq50XV0bkxJiYeEiNF5cwE5XsiOEkAUkXkUW51SSOVchjl8WKef604XFSRbzCGCYeCoESStv/p8QU1VPIM3knNDynctnBRfsEYhgSlNCIGgQv2UCkvGIHZgteMh1nBW9W4F16RAM6yDVV7amZTaYQcr59cuuhhWRTWBvAMLxQGeyFSHOLnh0MvUskz5RF+fbRYDEy0mZgqQYUHOLhr//b6rGoqeaLqQG0pw3PrBbyA+4EQUkRmhvgqNUfICUipKK4OKUqIJVPKB0jpEhjmWWp64jdbKmVZZNYogcJm493gsifOqhDyeh9GYR/FM7sW+DA5CKR0MSK3tvKZkpwB5gRE4tjFEr7RL0iWBGV51vHFCyupNGWWPqLgnoer9mtyEGSJAzwLllDTGzyznDjRN/CwOFkoFb4bm0eVIXICgpvdGoEvrF7fC89zfLkkeV5HbOhWiTwTpKYvCAJLGshRdXtKMKAWlyxq+MPQLk1h66g5RE5ABJYNFrqY3wvJklJRUKg5ZWLFXIA86yek2uDOPkBNb3CM5Pf7DL2QyIrUGiLH+xC5Bmmm/ARnHUhC6PnzxWDK0RH5HuIjZGy27erU9AZ0dTIWXyG+NpBBrSFySxZw220IqeUPFoS6jVAPNadM7yDsgNB1qOkLuAziMYIb1PQGA75wIaKGPyAb+9oF16g5RE5ALIQ+tSyLWoWDEAK6aXW3JlK9VJoyx1oyvVkNdvo5KXXDAVkdnaKmNwx0xjH98w3JNmTCm+Bc9hKVhsgJSI9pvp9Vdd++jmq6AXB2/HHrhcs5aTkVDv0DFzoHvKdq/mQsKX/4t7KJLDpOJW+IbAvMGoMkxfwAWZB8DT7W1diTE+WcgKz6pK1bs6z3daPwmJDsSKt6ZsCyjlLJMz0DsDGZ8SdlDROBjOb8YeWOjptU8kTXusuaazu7oJrfEnQvdkpVcUn6PTVHyAkIIW7br/Unklni0EJIZ1WgGsauZR+fvUglz6zY0dGfVp09ybRNlfwgi3k8YSbvJJ29VMoLt9v6rZVQL7hOYUubndHJGclBtzn1byqNMCogi09/2nFb01/oj+f/5TyjauBOKtPcZ1r7qZQ3f2lRfxZPWi2anp8TSDAGExZMa2jr8u03L1M5L7q3Xc+iAeuHRl/ScvPcjSLDBnZS/cjtNHd2v3171Ewbs9N5q7Pn4otVMx3btBsCsoRbk1FxG5dMVgMDqfTpXl1/tuFMa5zKefPROdX59qLQBwLnNog8Wy1OcjB1N+QEsW/QsFNZuO35Xb1v98QLX4/Sx+O3wqujrQ6013ABUWI8+AaqBjAH01+ghL22+5X2PirnMG7r+esbnae/V1neauvGSoHjigTcVU7UGFm2DeK4ttxKpQ+mLPvl+o/PjnkAkw9HTqSMmVHhyAMx9iFcSh/BHTfLceO/C8mKjApBf9zszGhoY92m9sN+BGOY9AeD7eGniv8OTaOB4dgyTsQd9wS+IQu4lciYdkI7CLrNH3Rvbb9FL41i0tbzVP2iWJkobpN5fmM4IJfJskTP1Bk8A9HQmbpmGDBrWqdVCN/Yd7PjxKGOXn+bmbto3feVVcVB9qehIL8EJy8nChwgr0O2xxBnhGU5eP2CfYbl/m4gBRsbtneMORP9oGpjpcCsiKzHHfdOPiQ/wMniyFEu2dbiTQCAeN/vavC466BGYLttXc9fmXBXMGlAhiHHur+sq6uPiUI9z7CVHMPwBnLSuuN8FuC48/Oaz1ylt94XfrW5ouyprwWfYRkwNyCyYYjwkBHows1fa+tV/fzGxlv39b9gqvfPmQ+i/HK8KlcBjhHwfl8HEHyOd1JnuzZd66S3TTPNNNP8/wDAfwDG7G0m9LKBpwAAAABJRU5ErkJggg==) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">消息的慢速查找<code>_objc_msgSend_uncached</code></h2>
<blockquote>
<p>由于上一章里我们是第一次进入快速查找，没有找到方法后，它进入了<code>_objc_msgSend_uncached</code>慢速查找。</p>
</blockquote>
<p><strong>在<code>cache</code>内查找<code>bucket_t</code>的过程中，如果查找了所有的缓存也无法命中的时候，接下来就要进入消息的慢速查找流程了，也就是由<code>汇编</code>查找 -> <code>C/C++</code>代码查找。</strong></p>
<h3 data-id="heading-1">慢速查找流程的图解：</h3>
<blockquote>
<p><code>__objc_msgSend_uncached</code>
此方法是进入慢速查找流程的起因，此方法是作为参数传递进<code>CacheLookup</code>的，如果<code>CacheLookup</code>查找不到<code>imp</code>的时候会执行<code>MissLabelDynamic</code>，也就是执行了<code>__objc_msgSend_uncached</code>。</p>
</blockquote>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TB
subgraph C++语言
A[__lookUpImpOrForward] --> B[getMethodNoSuper_nolock] -->  C[findMethodInSortedMethodList] --> D[log_and_fill_cache] --> E[insert]
end
subgraph 汇编语言
F[__objc_msgSend] --> G[CacheLookUp] --> |无法命中缓存|H[__objc_msgSend_uncached] --> I[MethodTableLookup] -->J[TailCallFunctionPointer x7]
end

I -.-> |具体实现流程| A
</code></pre>
<h3 data-id="heading-2">慢速查找<code>__objc_msgSend_uncached</code>的流程:</h3>
<ul>
<li>
<p>1⃣ 在<code>CacheLookup</code>汇编中，当无法找到缓存的时候，会执行<code>MissLabelDynamic</code>，也就是<code>__objc_msgSend_uncached</code></p>
</li>
<li>
<p>2⃣ 汇编中<code>__objc_msgSend_uncached</code>会执行<code>MethodTableLookup</code>和<code>TailCallFunctionPointer x17</code></p>
</li>
<li>
<p>3⃣ <code>MethodTableLookup</code>执行四个指令，将<code>x16</code>保存类地址移到<code>x2</code>，给<code>x3</code>赋值<code>#3</code>，跳转到<code>c++</code>源码中的<code>lookUpImpOrForward</code>方法，将<code>x0</code>移到<code>x17</code></p>
<ul>
<li>
<p>①<code>lookUpImpOrForward</code>，找到关键代码，是一个死循环查找<code>for (unsigned attempts = unreasonableClassCount();;)</code></p>
</li>
<li>
<p>② 加线程锁、进入<code>二分查找法</code></p>
</li>
<li>
<p>③ 如果找到，<code>log_and_fill_cache</code>,将找到的<code>imp</code>插入缓存，下一次<code>objc_msg_Send</code>将进行<code>快速</code>查找</p>
</li>
<li>
<p>④ 如果找不到，通过<code>isa</code>的查找链一直向上查找：共享缓存 -> <code>methodList</code> -> 父类 -> <code>NSObject</code> -> <code>nil</code> - > 跳出循环。最终都找不到的话，也就是<code>superclass=nil</code>的时候，将<code>imp = forward_imp</code>，进入<code>消息转发流程</code>(<strong>下一节内容</strong>)。</p>
</li>
</ul>
</li>
<li>
<p>4⃣ <code>TailCallFunctionPointer x17</code>，拿到上一步的查找结果将跳转至寄存器<code>x17</code></p>
</li>
</ul>
<h2 data-id="heading-3"><code>__objc_msgSend_uncached</code>源代码分析</h2>
<p>汇编源代码:</p>
<pre><code class="hljs language-c++ copyable" lang="c++">STATIC_ENTRY __objc_msgSend_uncached
UNWIND __objc_msgSend_uncached, FrameWithNoSaves

<span class="hljs-comment">//调用C++代码执行慢速查找流程</span>
MethodTableLookup
<span class="hljs-comment">//跳转到x17寄存器，等待汇编后续逻辑处理</span>
TailCallFunctionPointer x17

END_ENTRY __objc_msgSend_uncached
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4"><code>MethodTableLookup</code></h3>
<blockquote>
<p>保存信息方法，<code>x0</code>是<code>receiver</code>，<code>x1</code>是<code>_cmd</code>,即<code>sel</code>，先将<code>x16</code>（LGPerson类）存在<code>x2</code>寄存器，将<code>0x03</code>存在<code>x3</code>寄存器，然后跳转至关键方法<code>lookUpImpOrForward</code>，这个方法返回值在汇编的角度来看是储存在<code>x0</code>寄存器的，所以当<code>lookUpImpOrForward</code>执行完成，将返回值<code>x0</code>存入<code>x17</code>.</p>
</blockquote>
<p>c++源代码:</p>
<pre><code class="hljs language-c++ copyable" lang="c++">.macro MethodTableLookup
SAVE_REGS MSGSEND

<span class="hljs-comment">// lookUpImpOrForward(obj, sel, cls, behavior)</span>
<span class="hljs-comment">// receiver and selector already in x0 and x1</span>
<span class="hljs-comment">//lookUpImpOrForward方法需要4个参数：</span>
<span class="hljs-comment">//obj      = x0</span>
<span class="hljs-comment">//sel      = x1</span>
<span class="hljs-comment">//cls      = x2</span>
<span class="hljs-comment">//behavior = x3 = 3</span>
movx2, x16
movx3, #<span class="hljs-number">3</span>
<span class="hljs-comment">//bl：跳转指令，并将回家的路存在x30寄存器（lr）</span>
bl_lookUpImpOrForward

<span class="hljs-comment">// 经过_lookUpImpOrForward拿到的返回值（IMP）将存在x0位置</span>
<span class="hljs-comment">// 将x0赋值给x17</span>
movx17, x0

RESTORE_REGS MSGSEND

.endmacro
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><code>TailCallFunctionPointer</code></h3>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-comment">//A12以上芯片（支持arm64e结构）</span>
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> __has_feature(ptrauth_calls)</span>

<span class="hljs-comment">//通过慢速查找流程找到了IMP，那么这里就是将跳转至寄存器x17</span>
<span class="hljs-comment">//以提供后续汇编继续执行</span>
.macro TailCallFunctionPointer
<span class="hljs-comment">// $0 表示的是参数x17</span>
braaz$<span class="hljs-number">0</span>
.endmacro
<span class="hljs-meta">#<span class="hljs-meta-keyword">else</span></span>
.macro TailCallFunctionPointer
<span class="hljs-comment">// $0 表示的是参数x17</span>
br$<span class="hljs-number">0</span>
.endmacro
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论：</p>
<blockquote>
<p>当快速查找流程无法命中的时候会进入慢速查找流程<br>
慢速查找流程<code>__objc_msgSend_uncached</code>会执行2条指令，<code>MethodTableLookup</code>去查找并返回<code>imp</code>，<code>TailCallFunctionPointer</code>跳转至<code>x17</code>寄存器，也就是<code>imp</code>所在的寄存器<br>
慢速查找流程将会进入<code>C++</code>中执行，然后通过<code>x0</code>寄存器返回，继续在汇编中向下执行，方法查找流程最终会跳转至x17寄存器（无论是慢速查找还是快速查找。</p>
</blockquote>
<h2 data-id="heading-6"><code>lookUpImpOrForward</code>（慢速查找流程核心）</h2>
<h3 data-id="heading-7"><code>lookUpimpOrForward</code>流程的图解：</h3>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
    A1(["消息慢速查找"])
    A2["_objc_msgSend_uncached"]
    A3["MethodTableLookup<br>整理参数:obj,sel,cls,behavior"]
    A["_lookUpImpOrForward"]
    B&#123;"!cls->isInitialized()<br>类是否初始化<br>"&#125;
    D&#123;"checkIsknownClass(cls)<br>是否注册类是否<br>被lldb加载的类<br>"&#125;
    C["behaviour |= LOOKUP_NOCACHE<br>不缓存任何方法"]
    E["报错 Attempt to use unknown"]
    E1["realizeAndInitializeIfNeeded_locked<br>将此类相关的父类与元类递归初始化"]
    
    F&#123;"cls->isRealized()<br>类是否实现"&#125;
    G["realizeClassMaybeSwiftAndLeaveLocked<br>实现类和isa走位链与继承链相关联的类"]
    H&#123;"cls->isInitialized()<br>类是否初始化"&#125;
    I["initializeAndLeaveLocked<br>主要是类与父类的初始化,<br>主要是给类对象使用,如类方法"]
    I1["curClass = cls"]
    I2&#123;"for(unsigned attempts = unreasonableClassCount();;)<br>循环遍历类"&#125;
    
    J&#123;"curClass->cache.isConstantOptimizedCache<br>是否有共享缓存,<br>由_bucketsAndMaybeMask第一位决定,<br>1是有共享缓存"&#125;
    J1["getMethodNoSuper_nolock"]
    J2["search_method_list_inline"]
    K["imp=cache_getImp<br>去缓存中查询"]
    
    L["meth = getMethodNoSuper_nolock<br>二分法查询列表"]
    M&#123;"imp是否存在"&#125;
    
    N&#123;"meth是否查找到了IMP"&#125;
    S["done流程"]
    S1&#123;"(behavior & LOOKUP_NOCACHE) == 0<br>是否可以缓存imp"&#125;
    T["curClass = curClass-><br>cache.preoptFallbackClass()"]
    
    R&#123;"curClass=curClass->getSuperClass()<br>将父类赋值给curClass<br>curClass == nil<br>判断curClass是否为空nil"&#125;
 
    O["log_and_fill_cache<br>插入缓存"]
    O1["done_unlock流程"]
    O2&#123;"((behavior & LOOKUP_NIL) && <br>imp == forward_imp)) == 1<br>"&#125;
  
    P["imp = forward_imp<br>跳出循环"]
    
    Q["imp = cache_getImp(curClass, sel)<br>去汇编中执行,父类的缓存中查找imp"]
    Q1["GetClassFromIsa_p16 p0, 0"]
    Q2["CacheLookup缓存快速查找<br>具体看上一节"]
    Q3["LGetImpMissDynamic<br>找到父类的快速查找方法"]
    
    V&#123;"imp == forward_imp"&#125;
    W1&#123;"(behavior & LOOKUP_RESOLVER)<br>遍历完了父类都没有找到imp"&#125;
    W["behavior ^= LOOKUP_RESOLVER;<br>imp=resolveMethod_locked<br>动态方法决议"]
    W2(["动态方法决议,下一节重点说明"])
    
    Y&#123;"imp是否存在"&#125;
    X["return imp"]
    X1["return nil"]
    Z(["TailCallFunctionPointer x17"])
    A1 --> A2
    A2 --> A3
    A3 --> A
    A --> B 
    
    B -->|是| D
    B -->|否| C 
    C --> D
    
    D -->|是| E1
    E1 --> F
    
    D -->|否| E
    F -->|否| G
    F -->|是| H
    H -->|否| I
    H -->|是| I1
    I1 --> I2
    I2 -->|是| J
    I2 -->|否| W1
    W1 --> |是| W
    W --> W2
    W1 --> |否| S
    J -->|否| J1
    J1 --> J2
    J2 -->|否| L
    
    L --> N
    N -->|否| R
    R -->|否| Q
  
    V -->|是| Y
    Y -->|否| I2
    V -->|否| I2

    J -->|是| K
    K --> M 
    M -->|是| O1
    M -->|否| T
    T --> Q
    Q --> Q1
    Q1 --> Q2
    Q2 --> Q3
    Q3 --> V
    
    
    N -->|是| S
   
    S1 -->|是| O
    O --> O1
    O1 --> O2
    O2 -->|是| X
    O2 -->|否| X1
    
    R -->|是| P
    P --> I2
    
    Y -->|是| S
    S --> S1
    X --> Z
</code></pre>
<h3 data-id="heading-8"><code>lookUpimpOrForward</code>的源码分析</h3>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-comment">// 缓存 找不到 - lookUpImpOrForward - 慢速 - methodlist</span>
<span class="hljs-comment">// 汇编 缓存 参数未知</span>
<span class="hljs-function">NEVER_INLINE
IMP <span class="hljs-title">lookUpImpOrForward</span><span class="hljs-params">(id inst, SEL sel, Class cls, <span class="hljs-keyword">int</span> behavior)</span>
</span>&#123;
    <span class="hljs-comment">//创建forward_imp，并给定默认值_objc_msgForward_impcache(具体在汇编objc-msg-arm64.s:跳转到__objc_msgForward)</span>
    <span class="hljs-keyword">const</span> IMP forward_imp = (IMP)_objc_msgForward_impcache;
    <span class="hljs-comment">//创建imp，用于接收通过sel查找的imp</span>
    IMP imp = nil;
    <span class="hljs-comment">//创建要查找的类，这个类通过isa的指向关系是会一直变化的，</span>
    <span class="hljs-comment">//直到最终指向NSObject的父类nil为止</span>
    Class curClass;

    runtimeLock.<span class="hljs-built_in">assertUnlocked</span>();

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">slowpath</span>(!cls-><span class="hljs-built_in">isInitialized</span>())) &#123;
        <span class="hljs-comment">/**
        发送到类的第一条消息通常是 +new 或 +alloc 或 +self
        但是，此时该类尚未初始化，此时behavior = 3｜8 = 11
        当向将上+new等这些方法inset进缓存的时候
        不满足behavior & LOOKUP_NOCACHE) == 0这个条件，8 & 11 = 8
        所以上述这些方法不会加载进缓存。
        
        如果类已经初始化了，就不会修改behavior的值了，behavior=3
        我们自定义的方法是可以正常加载进缓存的。
        */</span>
        behavior |= LOOKUP_NOCACHE;
    &#125;

    <span class="hljs-comment">// runtimeLock 在 isRealized 和 isInitialized 检查期间被持有</span>
    <span class="hljs-comment">// 防止与并发实现竞争。</span>
    runtimeLock.<span class="hljs-built_in">lock</span>();

    <span class="hljs-comment">//检查类是否被注册了</span>
    <span class="hljs-comment">//防止人为制造类，进行CFI攻击</span>
    <span class="hljs-built_in">checkIsKnownClass</span>(cls);

    <span class="hljs-comment">/**初始化跟cls实例对象在isa指向图中的每一个类（class和metaClass）
    以便后续自己类里面找不到方法去父类里面找
    依次向上找
    所以在此处对所有相关的类进行了初始化
    */</span>
    cls = <span class="hljs-built_in">realizeAndInitializeIfNeeded_locked</span>(inst, cls, behavior & LOOKUP_INITIALIZE);
    <span class="hljs-comment">// runtimeLock may have been dropped but is now locked again</span>
    runtimeLock.<span class="hljs-built_in">assertLocked</span>();
    <span class="hljs-comment">//curClass为当前实例对象的类</span>
    curClass = cls;

    <span class="hljs-comment">/**
    * 循环查找类对象的methodList，当前类没有的话就找父类
    * 父类没有就找父类的父类，一直找到NSObject类
    * 如果NSObject都找不到的话最终curClass会指向nil
    * 将事先准备好的forward_imp赋值给imp
    * 然后结束慢速查找流程，接下来进入Runtime消息转发机制
    */</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">unsigned</span> attempts = <span class="hljs-built_in">unreasonableClassCount</span>();;) &#123;
        <span class="hljs-keyword">if</span> (curClass->cache.<span class="hljs-built_in">isConstantOptimizedCache</span>(<span class="hljs-comment">/* strict */</span><span class="hljs-literal">true</span>)) &#123;
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> CONFIG_USE_PREOPT_CACHES</span>
            <span class="hljs-comment">/**
            * 第一步先找共享缓存里面有没有我们的方法
            * 通常情况下我们的自定义方法不会出现在共享缓存中
            */</span>
            imp = <span class="hljs-built_in">cache_getImp</span>(curClass, sel);
            <span class="hljs-keyword">if</span> (imp) <span class="hljs-keyword">goto</span> done_unlock;
            curClass = curClass->cache.<span class="hljs-built_in">preoptFallbackClass</span>();
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">/**
            *在当前类的方法列表里面查找，这是重点
            *查找算法是二分法
            */</span>
            Method meth = <span class="hljs-built_in">getMethodNoSuper_nolock</span>(curClass, sel);
            <span class="hljs-keyword">if</span> (meth) &#123;
                imp = meth-><span class="hljs-built_in">imp</span>(<span class="hljs-literal">false</span>);
                <span class="hljs-keyword">goto</span> done;
            &#125;
            <span class="hljs-comment">/**
            *如果当前类找不到，取将curClass指向superclass
            *查询父类的methodList，一直找到NSObject的父类nil为止
            * 将事先准备好的forward_imp赋值给imp
            * 然后结束慢速查找流程，接下来进入Runtime消息转发机制
            * 结束循环遍历
            */</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">slowpath</span>((curClass = curClass-><span class="hljs-built_in">getSuperclass</span>()) == nil)) &#123;
                imp = forward_imp;
                <span class="hljs-keyword">break</span>;
            &#125;
        &#125;

        <span class="hljs-comment">// 类列表中的内存损坏</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">slowpath</span>(--attempts == <span class="hljs-number">0</span>)) &#123;
            _objc_fatal(<span class="hljs-string">"Memory corruption in class list."</span>);
        &#125;

        <span class="hljs-comment">// 在父类的缓存中查找，这里再次进入汇编查找流程</span>
        imp = <span class="hljs-built_in">cache_getImp</span>(curClass, sel);
        <span class="hljs-comment">//如果没有找到，将默认的forward_imp赋值给imp</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">slowpath</span>(imp == forward_imp)) &#123;
            <span class="hljs-comment">// Found a forward:: entry in a superclass.</span>
            <span class="hljs-comment">// Stop searching, but don't cache yet; call method</span>
            <span class="hljs-comment">// resolver for this class first.</span>
            <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-comment">//如果找到了</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">fastpath</span>(imp)) &#123;
            <span class="hljs-comment">//将找到的method插入到缓存中，以便下次查找使用快速缓存查找</span>
            <span class="hljs-keyword">goto</span> done;
        &#125;
    &#125;

    <span class="hljs-comment">// No implementation found. Try method resolver once.</span>

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">slowpath</span>(behavior & LOOKUP_RESOLVER)) &#123;
        behavior ^= LOOKUP_RESOLVER;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">resolveMethod_locked</span>(inst, sel, cls, behavior);
    &#125;

<span class="hljs-comment">//找到了sel对应的imp，将method方法加载进缓存</span>
 done:
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">fastpath</span>((behavior & LOOKUP_NOCACHE) == <span class="hljs-number">0</span>)) &#123;
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> CONFIG_USE_PREOPT_CACHES</span>
        <span class="hljs-keyword">while</span> (cls->cache.<span class="hljs-built_in">isConstantOptimizedCache</span>(<span class="hljs-comment">/* strict */</span><span class="hljs-literal">true</span>)) &#123;
            cls = cls->cache.<span class="hljs-built_in">preoptFallbackClass</span>();
        &#125;
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
        <span class="hljs-built_in">log_and_fill_cache</span>(cls, imp, sel, inst, curClass);
    &#125;
 done_unlock:
    runtimeLock.<span class="hljs-built_in">unlock</span>();
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">slowpath</span>((behavior & LOOKUP_NIL) && imp == forward_imp)) &#123;
        <span class="hljs-keyword">return</span> nil;
    &#125;
    <span class="hljs-keyword">return</span> imp;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9"><code>realizeClassWithoutSwift</code></h4>
<blockquote>
<p>只列出了2行关键源码，用来表示递归初始化类和元类</p>
</blockquote>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">static</span> Class <span class="hljs-title">realizeClassWithoutSwift</span><span class="hljs-params">(Class cls, Class previously)</span>
</span>&#123;
    supercls = <span class="hljs-built_in">realizeClassWithoutSwift</span>(<span class="hljs-built_in">remapClass</span>(cls-><span class="hljs-built_in">getSuperclass</span>()), nil);
    metacls = <span class="hljs-built_in">realizeClassWithoutSwift</span>(<span class="hljs-built_in">remapClass</span>(cls-><span class="hljs-built_in">ISA</span>()), nil);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10"><code>getMethodNoSuper_nolock</code>(二分查找流程)</h4>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">method_t</span> *
<span class="hljs-title">getMethodNoSuper_nolock</span><span class="hljs-params">(Class cls, SEL sel)</span>
</span>&#123;
    runtimeLock.<span class="hljs-built_in">assertLocked</span>();

    <span class="hljs-built_in">ASSERT</span>(cls-><span class="hljs-built_in">isRealized</span>());
    
    <span class="hljs-comment">//拿到cls的data()里面存的methods()</span>
    <span class="hljs-keyword">auto</span> <span class="hljs-keyword">const</span> methods = cls-><span class="hljs-built_in">data</span>()-><span class="hljs-built_in">methods</span>();
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">auto</span> mlists = methods.<span class="hljs-built_in">beginLists</span>(),
              end = methods.<span class="hljs-built_in">endLists</span>();
         mlists != end;
         ++mlists)
    &#123;
        <span class="hljs-comment">//进入search_method_list_inline修复为有序list</span>
        <span class="hljs-comment">//从方法列表中找当前sel</span>
        <span class="hljs-comment">//类中自定义的方法第一次循环的时候走这里，存在methods.beginLists()</span>

        <span class="hljs-keyword">method_t</span> *m = <span class="hljs-built_in">search_method_list_inline</span>(*mlists, sel);
        <span class="hljs-keyword">if</span> (m) <span class="hljs-keyword">return</span> m;
    &#125;

    <span class="hljs-keyword">return</span> nil;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11"><code>search_method_list_inline</code></h4>
<blockquote>
<p>修复函数，来函是<code>methodList</code>变得有序</p>
</blockquote>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function">ALWAYS_INLINE <span class="hljs-keyword">static</span> <span class="hljs-keyword">method_t</span> *
<span class="hljs-title">search_method_list_inline</span><span class="hljs-params">(<span class="hljs-keyword">const</span> <span class="hljs-keyword">method_list_t</span> *mlist, SEL sel)</span>
</span>&#123;
    <span class="hljs-keyword">int</span> methodListIsFixedUp = mlist-><span class="hljs-built_in">isFixedUp</span>();
    <span class="hljs-keyword">int</span> methodListHasExpectedSize = mlist-><span class="hljs-built_in">isExpectedSize</span>();
    
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">fastpath</span>(methodListIsFixedUp && methodListHasExpectedSize)) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">findMethodInSortedMethodList</span>(sel, mlist);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// Linear search of unsorted method list</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">auto</span> *m = <span class="hljs-built_in">findMethodInUnsortedMethodList</span>(sel, mlist))
            <span class="hljs-keyword">return</span> m;
    &#125;

    <span class="hljs-keyword">return</span> nil;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12"><code>findMethodInSortedMethodList</code>(已经排好序的<code>methodlist</code>)</h4>
<blockquote>
<p><code>isSmallList</code>代表的是<code>m1</code>的电脑。</p>
</blockquote>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function">ALWAYS_INLINE <span class="hljs-keyword">static</span> <span class="hljs-keyword">method_t</span> *
<span class="hljs-title">findMethodInSortedMethodList</span><span class="hljs-params">(SEL key, <span class="hljs-keyword">const</span> <span class="hljs-keyword">method_list_t</span> *list)</span>
</span>&#123;
    <span class="hljs-keyword">if</span> (list-><span class="hljs-built_in">isSmallList</span>()) &#123;
        <span class="hljs-keyword">if</span> (CONFIG_SHARED_CACHE_RELATIVE_DIRECT_SELECTORS && objc::<span class="hljs-built_in">inSharedCache</span>((<span class="hljs-keyword">uintptr_t</span>)list)) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">findMethodInSortedMethodList</span>(key, list, [](<span class="hljs-keyword">method_t</span> &m) &#123; <span class="hljs-keyword">return</span> m.<span class="hljs-built_in">getSmallNameAsSEL</span>(); &#125;);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">findMethodInSortedMethodList</span>(key, list, [](<span class="hljs-keyword">method_t</span> &m) &#123; <span class="hljs-keyword">return</span> m.<span class="hljs-built_in">getSmallNameAsSELRef</span>(); &#125;);
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">findMethodInSortedMethodList</span>(key, list, [](<span class="hljs-keyword">method_t</span> &m) &#123; <span class="hljs-keyword">return</span> m.<span class="hljs-built_in">big</span>().name; &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">findMethodInSortedMethodList（二分查找真正的实现方法）</h4>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">template</span><class getNameFunc>
ALWAYS_INLINE <span class="hljs-keyword">static</span> <span class="hljs-keyword">method_t</span> *
<span class="hljs-title">findMethodInSortedMethodList</span><span class="hljs-params">(SEL key, <span class="hljs-keyword">const</span> <span class="hljs-keyword">method_list_t</span> *list, <span class="hljs-keyword">const</span> getNameFunc &getName)</span>
</span>&#123;
    <span class="hljs-built_in">ASSERT</span>(list);
    <span class="hljs-comment">//开始位置：0</span>
    <span class="hljs-keyword">auto</span> first = list-><span class="hljs-built_in">begin</span>();
    <span class="hljs-comment">//base开始也为0</span>
    <span class="hljs-keyword">auto</span> base = first;
    <span class="hljs-comment">//probe也为0</span>
    <span class="hljs-keyword">decltype</span>(first) probe;
    <span class="hljs-comment">//要查找imp对应的sel</span>
    <span class="hljs-keyword">uintptr_t</span> keyValue = (<span class="hljs-keyword">uintptr_t</span>)key;
    <span class="hljs-comment">//list的个数</span>
    <span class="hljs-keyword">uint32_t</span> count;
    
    <span class="hljs-comment">/**
    * 举例：假设要查找的sel在第7位
    * 首先count = list.count,这里假定count=8
    * 进入循环，probe = base + （ 8 >> 1 ） = 0 + 4 = 4
    * 那么第一次查找的范围就是4-8，匹配元素位置是4，判定结果keyValue（7）> prebeValue(4)，未匹配
    * 满足keyValue > probeValue，base = probe + 1 = 4 + 1 = 5，count-- = 7
    * 第二次进入循环，此时count = 7 >> 1 = 3, probe = 5 + (3 >> 1) = 6
    * 第二次查找的范围是6-7，匹配元素位置是6，判定结果keyValue（7）> prebeValue(6)，未匹配
    * 满足keyValue > probeValue，base = probe + 1 = 6 + 1 = 7，count-- = 2
    * 第三次进入循环，此时count = 2 >> 1 = 1, probe = 7 + (1 >> 1) = 7
    * 第三次查找的元素是7，匹配，返回imp
    */</span>
    <span class="hljs-keyword">for</span> (count = list->count; count != <span class="hljs-number">0</span>; count >>= <span class="hljs-number">1</span>) &#123;
        probe = base + (count >> <span class="hljs-number">1</span>);
        
        <span class="hljs-keyword">uintptr_t</span> probeValue = (<span class="hljs-keyword">uintptr_t</span>)<span class="hljs-built_in">getName</span>(probe);
        
        <span class="hljs-keyword">if</span> (keyValue == probeValue) &#123;
            <span class="hljs-comment">//向前寻找第一个出现的imp，为了避免分类方法于主类方法相同时问题</span>
            <span class="hljs-comment">//这也就是为什么分类方法会被加载的原因</span>
            <span class="hljs-keyword">while</span> (probe > first && keyValue == (<span class="hljs-keyword">uintptr_t</span>)<span class="hljs-built_in">getName</span>((probe - <span class="hljs-number">1</span>))) &#123;
                probe--;
            &#125;
            <span class="hljs-keyword">return</span> &*probe;
        &#125;
        
        <span class="hljs-keyword">if</span> (keyValue > probeValue) &#123;
            base = probe + <span class="hljs-number">1</span>;
            count--;
        &#125;
    &#125;
    
    <span class="hljs-keyword">return</span> nil;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">log_and_fill_cache(缓存填充)</h4>
<p>如果记录器允许，调用cache的insert方法，将其插入缓存，下一次的查找就会进行快速缓存查找了。</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span>
<span class="hljs-title">log_and_fill_cache</span><span class="hljs-params">(Class cls, IMP imp, SEL sel, id receiver, Class implementer)</span>
</span>&#123;
<span class="hljs-meta">#<span class="hljs-meta-keyword">if</span> SUPPORT_MESSAGE_LOGGING</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">slowpath</span>(objcMsgLogEnabled && implementer)) &#123;
        <span class="hljs-keyword">bool</span> cacheIt = <span class="hljs-built_in">logMessageSend</span>(implementer-><span class="hljs-built_in">isMetaClass</span>(), 
                                      cls-><span class="hljs-built_in">nameForLogging</span>(),
                                      implementer-><span class="hljs-built_in">nameForLogging</span>(), 
                                      sel);
        <span class="hljs-keyword">if</span> (!cacheIt) <span class="hljs-keyword">return</span>;
    &#125;
<span class="hljs-meta">#<span class="hljs-meta-keyword">endif</span></span>
    cls->cache.<span class="hljs-built_in">insert</span>(sel, imp, receiver);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论:</p>
<blockquote>
<p><code>lookUpImpOrForward</code>，此过程为慢速查找流程，通过死循环的方式不断遍历来查找<code>imp</code>，对于全局性来讲，首先去找共享缓存，然后查自己的<code>methodList</code>，如果自己没有，找父类，父类没有，找<code>NSObject</code>，<code>NSObject</code>没有，会指向<code>nil</code>，最终跳出来。
流程简化：<code>共享缓存</code> -> <code>methodList</code> -> <code>父类</code> -> <code>NSObject</code> -> <code>nil</code>- ><code>跳出循环</code></p>
</blockquote>
<h2 data-id="heading-15">二分法查找法</h2>
<blockquote>
<p>使用<code>C++</code>代码还原<code>二分查找法</code>,假设二分法要找的内容是第3</p>
</blockquote>
<p>案例代码：</p>
<pre><code class="hljs language-c++ copyable" lang="c++"><span class="hljs-meta">#<span class="hljs-meta-keyword">include</span> <span class="hljs-meta-string"><iostream></span></span>

<span class="hljs-keyword">using</span> <span class="hljs-keyword">namespace</span> std;

<span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">(<span class="hljs-keyword">int</span> argc, <span class="hljs-keyword">const</span> <span class="hljs-keyword">char</span>  argv[])</span> </span>&#123;

    <span class="hljs-keyword">auto</span> first = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">auto</span> base = first;
    <span class="hljs-keyword">decltype</span>(first) probe = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">uintptr_t</span> keyValue = <span class="hljs-number">3</span>;
    <span class="hljs-keyword">uint32_t</span> count;

     
    <span class="hljs-keyword">for</span> (count = <span class="hljs-number">8</span>; count != <span class="hljs-number">0</span>; count >>= <span class="hljs-number">1</span>) &#123;
    
        cout << <span class="hljs-string">"前=count: "</span><< count << <span class="hljs-string">"---probe: "</span> << probe << endl;
        <span class="hljs-comment">//1. base = 0, count = 8, probe = 0 + (8 >> 1) = 4</span>
        <span class="hljs-comment">//2. base = 0, count = 8 >> 1 = 4, probe = 0 + (4 >> 1) = 2</span>
        <span class="hljs-comment">//3. base = 3, count = 3 >> 1 = 1, probe = 3 + (1 >> 1) = 3;</span>
        probe = base + (count >> <span class="hljs-number">1</span>);
        cout << <span class="hljs-string">"后=count: "</span><< count << <span class="hljs-string">"---probe: "</span> << probe << endl;

        <span class="hljs-comment">//1: 3 != 4,没找到</span>
        <span class="hljs-comment">//2: 3 != 2,没找到</span>
        <span class="hljs-comment">//3: 3 == 3,找到了</span>
        <span class="hljs-keyword">if</span> (keyValue == probe) &#123;

            cout << <span class="hljs-string">"找到了=keyValue: "</span> << keyValue << <span class="hljs-string">"---probe: "</span> << probe << endl;
            <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
            
        &#125;
        <span class="hljs-keyword">else</span>&#123;

            cout << <span class="hljs-string">"没找到=keyValue: "</span> << keyValue << <span class="hljs-string">"---probe: "</span> << probe << endl;

        &#125;

       <span class="hljs-comment">//1: 3 < 4, base = 0,         count = 8;</span>
       <span class="hljs-comment">//2: 3 > 2, base = 2 + 1 = 3, count = 4 - 1 = 3;</span>
        <span class="hljs-keyword">if</span> (keyValue > probe) &#123;
            base = probe + <span class="hljs-number">1</span>;
            count--;
        &#125;
    &#125;

    <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>控制台打印结果：</p>
<pre><code class="hljs language-llvm copyable" lang="llvm">前<span class="hljs-operator">=</span>count: <span class="hljs-number">8</span>---probe: <span class="hljs-number">0</span>

后<span class="hljs-operator">=</span>count: <span class="hljs-number">8</span>---probe: <span class="hljs-number">4</span>

没找到<span class="hljs-operator">=</span>keyValue: <span class="hljs-number">3</span>---probe: <span class="hljs-number">4</span>

前<span class="hljs-operator">=</span>count: <span class="hljs-number">4</span>---probe: <span class="hljs-number">4</span>

后<span class="hljs-operator">=</span>count: <span class="hljs-number">4</span>---probe: <span class="hljs-number">2</span>

没找到<span class="hljs-operator">=</span>keyValue: <span class="hljs-number">3</span>---probe: <span class="hljs-number">2</span>

前<span class="hljs-operator">=</span>count: <span class="hljs-number">1</span>---probe: <span class="hljs-number">2</span>

后<span class="hljs-operator">=</span>count: <span class="hljs-number">1</span>---probe: <span class="hljs-number">3</span>

找到了<span class="hljs-operator">=</span>keyValue: <span class="hljs-number">3</span>---probe: <span class="hljs-number">3</span>

Program ended with exit code: <span class="hljs-number">0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结论：</p>
<blockquote>
<p>假设要查找的<code>sel</code>对应的在第<code>3</code>位 <br>
首先<code>count = list.count</code>,这里假定<code>count=8</code>
第一次进入循环，<code>probe = base + （ 8 >> 1 ） = 0 + 4 = 4</code></p>
<blockquote>
<p>那么第一次查找的范围就是<code>4-8</code>，匹配元素位置是<code>4</code>，判定结果<code>keyValue(3)</code> < <code>prebeValue(4)</code>，未匹配
不满足<code>keyValue</code> > <code>probeValue</code>，<code>base = 0，count = 8</code>；</p>
</blockquote>
<p>第二次进入循环，此时<code>count = 8 >> 1 = 4, probe = 0 + （4 >> 1） = 2</code></p>
<blockquote>
<p>第二次查找的范围是<code>1-4</code>，匹配元素位置是<code>4</code>，判定结果<code>keyValue(3)</code> > <code>prebeValue(4)</code>，未匹配
满足<code>keyValue</code> > <code>probeValue</code>，<code>base = probe + 1 = 2 + 1 = 3</code>，<code>count-- = 3</code></p>
</blockquote>
<p>第三次进入循环，此时<code>count = 3 >> 1 = 1</code>, <code>probe = 3 + （1 >> 1） = 3 </code></p>
<blockquote>
<p>第三次查找的元素是<code>3</code>，匹配，返回<code>imp</code></p>
</blockquote>
</blockquote></div>  
</div>
            