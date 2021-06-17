
---
title: 'React，优雅的捕获异常'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5984'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 05:30:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=5984'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAdCAYAAABcz8ldAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAhgSURBVGhD7Zp7bBTHHcdn33t7vvOdzy+ITVKDU0xIKG2ABCPTRCCaUiEVKWoqRJuASAhCitRCVKSoalFUKZBiSmmFRRJKRUnUtIpo+aNqGgwoOCmuFUIRzxjwE4zte+97drYzztji8HPvtkit/PnH+n1397Tz+83vN/PbMZhmmmmm+d+BoX8n5diihcGqgFQf5vk6BMAskWUlw3GyFnIvtqWSf91w7mKC3npfOLX7wYeiIa6BBWCOLLFRF2NB0JvIOP/80YG+k2ev6S699b/OzOfKBW5l5KsgyC4DCFQDnpEAdE1goc/dlNPc/Up7P711UiYNSMuyxeUzZPnHgGHWh5XADEkSAcdiN+AnEXIBhBComgFU0/xQR+jnj51sOUMf9Z0NKyL8S9+JPBEN8zuCMrsqGOA5QWAAyzLAxe53HBeYFgJp1c5Cx33nyIfpV3e+22/Sx32nev/sMCgVnmM4bjOniAtZWQAsz315EfsGQQc4hgWcjHkCmOj1rheuNn95cXwmDMiVp5etC/D8m5FwUWVQUYYGPh6mZYFUOgsGVa1pXvOZzVT2jRuH54RM230jEuI3RcIiL4l4UkxAJmuD/riVsqD7ct2m9nep7BtVTbVfZ0uE/UIk+CQflAHDjf8+Lg6MldYATGpH3c/Ul7p3dWXppVGM6eElJSHmnQWPbSlRlN1lJcUBjqNRnwJZVQO3B5P/uq5rK1d90pakckFcaKp5UJHY92JR8YlwkUDVySEZfGfQdO7E7Z8s2HL9TSoXTPXRud9nA8IBqSwcZgWeqpPj6BYw7yTbXBN9q2v9lQEq5zBmWA8vWLCptCi4tzwW8RQMQlFQATPLSh6vCSh/plJBkMyQBHZfWYnkKRgEktEVpTJXERN2Xzo4ex2VC6K6qXYpF5b3ypVRT8EgcAERSJXRbwCBOTFzXblM5RxGBaRt+ZPYA+LO0mgxz5K1Ig+UgAzKIuGnz39z6S+olDeaibaXRsU1RUFvgx+GwTWgPCaDgMw2XXpr9gwq50XV0bkxJiYeEiNF5cwE5XsiOEkAUkXkUW51SSOVchjl8WKef604XFSRbzCGCYeCoESStv/p8QU1VPIM3knNDynctnBRfsEYhgSlNCIGgQv2UCkvGIHZgteMh1nBW9W4F16RAM6yDVV7amZTaYQcr59cuuhhWRTWBvAMLxQGeyFSHOLnh0MvUskz5RF+fbRYDEy0mZgqQYUHOLhr//b6rGoqeaLqQG0pw3PrBbyA+4EQUkRmhvgqNUfICUipKK4OKUqIJVPKB0jpEhjmWWp64jdbKmVZZNYogcJm493gsifOqhDyeh9GYR/FM7sW+DA5CKR0MSK3tvKZkpwB5gRE4tjFEr7RL0iWBGV51vHFCyupNGWWPqLgnoer9mtyEGSJAzwLllDTGzyznDjRN/CwOFkoFb4bm0eVIXICgpvdGoEvrF7fC89zfLkkeV5HbOhWiTwTpKYvCAJLGshRdXtKMKAWlyxq+MPQLk1h66g5RE5ABJYNFrqY3wvJklJRUKg5ZWLFXIA86yek2uDOPkBNb3CM5Pf7DL2QyIrUGiLH+xC5Bmmm/ARnHUhC6PnzxWDK0RH5HuIjZGy27erU9AZ0dTIWXyG+NpBBrSFySxZw220IqeUPFoS6jVAPNadM7yDsgNB1qOkLuAziMYIb1PQGA75wIaKGPyAb+9oF16g5RE5ALIQ+tSyLWoWDEAK6aXW3JlK9VJoyx1oyvVkNdvo5KXXDAVkdnaKmNwx0xjH98w3JNmTCm+Bc9hKVhsgJSI9pvp9Vdd++jmq6AXB2/HHrhcs5aTkVDv0DFzoHvKdq/mQsKX/4t7KJLDpOJW+IbAvMGoMkxfwAWZB8DT7W1diTE+WcgKz6pK1bs6z3daPwmJDsSKt6ZsCyjlLJMz0DsDGZ8SdlDROBjOb8YeWOjptU8kTXusuaazu7oJrfEnQvdkpVcUn6PTVHyAkIIW7br/Unklni0EJIZ1WgGsauZR+fvUglz6zY0dGfVp09ybRNlfwgi3k8YSbvJJ29VMoLt9v6rZVQL7hOYUubndHJGclBtzn1byqNMCogi09/2nFb01/oj+f/5TyjauBOKtPcZ1r7qZQ3f2lRfxZPWi2anp8TSDAGExZMa2jr8u03L1M5L7q3Xc+iAeuHRl/ScvPcjSLDBnZS/cjtNHd2v3171Ewbs9N5q7Pn4otVMx3btBsCsoRbk1FxG5dMVgMDqfTpXl1/tuFMa5zKefPROdX59qLQBwLnNog8Wy1OcjB1N+QEsW/QsFNZuO35Xb1v98QLX4/Sx+O3wqujrQ6013ABUWI8+AaqBjAH01+ghL22+5X2PirnMG7r+esbnae/V1neauvGSoHjigTcVU7UGFm2DeK4ttxKpQ+mLPvl+o/PjnkAkw9HTqSMmVHhyAMx9iFcSh/BHTfLceO/C8mKjApBf9zszGhoY92m9sN+BGOY9AeD7eGniv8OTaOB4dgyTsQd9wS+IQu4lciYdkI7CLrNH3Rvbb9FL41i0tbzVP2iWJkobpN5fmM4IJfJskTP1Bk8A9HQmbpmGDBrWqdVCN/Yd7PjxKGOXn+bmbto3feVVcVB9qehIL8EJy8nChwgr0O2xxBnhGU5eP2CfYbl/m4gBRsbtneMORP9oGpjpcCsiKzHHfdOPiQ/wMniyFEu2dbiTQCAeN/vavC466BGYLttXc9fmXBXMGlAhiHHur+sq6uPiUI9z7CVHMPwBnLSuuN8FuC48/Oaz1ylt94XfrW5ouyprwWfYRkwNyCyYYjwkBHows1fa+tV/fzGxlv39b9gqvfPmQ+i/HK8KlcBjhHwfl8HEHyOd1JnuzZd66S3TTPNNNP8/wDAfwDG7G0m9LKBpwAAAABJRU5ErkJggg==) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第7天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>人无完人，所以代码总会出错，出错并不可怕，关键是怎么处理。<br>
我就想问问大家react的应用的错误怎么捕捉呢？ 这个时候：</p>
<ul>
<li>小白+++：怎么处理？</li>
<li>小白++： ErrorBoundary</li>
<li>小白+： ErrorBoundary, try catch</li>
<li>小黑#:  ErrorBoundary, try catch, window.onerror</li>
<li>小黑##: 这个是个严肃的问题，我知道N种处理方式，你有什么更好的方案?</li>
</ul>
<h2 data-id="heading-1">ErrorBoundary</h2>
<p>EerrorBoundary是16版本出来的，有人问那我的15版本呢，我不听我不听，反正我用16，当然15有<code>unstable_handleError</code>。</p>
<p>关于ErrorBoundary官网介绍比较详细，这个不是重点，重点是他能捕捉哪些异常。</p>
<ul>
<li>子组件的渲染</li>
<li>生命周期函数</li>
<li>构造函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ErrorBoundary</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">hasError</span>: <span class="hljs-literal">false</span> &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidCatch</span>(<span class="hljs-params">error, info</span>)</span> &#123;
    <span class="hljs-comment">// Display fallback UI</span>
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">hasError</span>: <span class="hljs-literal">true</span> &#125;);
    <span class="hljs-comment">// You can also log the error to an error reporting service</span>
    logErrorToMyService(error, info);
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state.hasError) &#123;
      <span class="hljs-comment">// You can render any custom fallback UI</span>
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Something went wrong.<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.props.children;
  &#125;
&#125;


<ErrorBoundary>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">MyWidget</span> /></span></span>
</ErrorBoundary>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开源世界就是好，早有大神封装了<a href="https://www.npmjs.com/package/react-error-boundary" target="_blank" rel="nofollow noopener noreferrer">react-error-boundary</a> 这种优秀的库。<br>
你只需要关心出现错误后需要关心什么，还以来个 <code>Reset</code>, 完美。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;ErrorBoundary&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-error-boundary'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ErrorFallback</span>(<span class="hljs-params">&#123;error, resetErrorBoundary&#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">role</span>=<span class="hljs-string">"alert"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Something went wrong:<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">pre</span>></span>&#123;error.message&#125;<span class="hljs-tag"></<span class="hljs-name">pre</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;resetErrorBoundary&#125;</span>></span>Try again<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;

<span class="hljs-keyword">const</span> ui = (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ErrorBoundary</span>
    <span class="hljs-attr">FallbackComponent</span>=<span class="hljs-string">&#123;ErrorFallback&#125;</span>
    <span class="hljs-attr">onReset</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
      // reset the state of your app so the error doesn't happen again
    &#125;&#125;
  >
    <span class="hljs-tag"><<span class="hljs-name">ComponentThatMayError</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">ErrorBoundary</span>></span></span>
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遗憾的是，error boundaries并不会捕捉这些错误：</p>
<ul>
<li>事件处理程序</li>
<li>异步代码 (e.g. setTimeout or requestAnimationFrame callbacks)</li>
<li>服务端的渲染代码</li>
<li>error boundaries自己抛出的错误</li>
</ul>
<p>原文可见参见官网<a href="https://reactjs.org/docs/error-boundaries.html#introducing-error-boundaries" target="_blank" rel="nofollow noopener noreferrer">introducing-error-boundaries</a></p>
<p>本文要捕获的就是 事件处理程序的错误。<br>
官方其实也是有方案的<a href="https://reactjs.org/docs/error-boundaries.html#how-about-event-handlers" target="_blank" rel="nofollow noopener noreferrer">how-about-event-handlers</a>， 就是 try catch.<br>
但是，那么多事件处理程序，我的天，得写多少，。。。。。。。。。。。。。。。。。。。。</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// Do something that could throw</span>
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
      <span class="hljs-built_in">this</span>.setState(&#123; error &#125;);
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">Error Boundary 之外</h2>
<p>我们先看看一张表格，罗列了我们能捕获异常的手段和范围。</p>













































<table><thead><tr><th>异常类型</th><th align="center">同步方法</th><th align="center">异步方法</th><th align="center">资源加载</th><th align="center">Promise</th><th align="center">async/await</th></tr></thead><tbody><tr><td>try/catch</td><td align="center">√</td><td align="center"></td><td align="center"></td><td align="center"></td><td align="center">√</td></tr><tr><td>window.onerror</td><td align="center">√</td><td align="center">√</td><td align="center"></td><td align="center"></td><td align="center"></td></tr><tr><td>error</td><td align="center">√</td><td align="center">√</td><td align="center">√</td><td align="center"></td><td align="center"></td></tr><tr><td>unhandledrejection</td><td align="center"></td><td align="center"></td><td align="center"></td><td align="center">√</td><td align="center">√</td></tr></tbody></table>
<h3 data-id="heading-3">try/catch</h3>
<p>可以捕获同步和async/await的异常。</p>
<h3 data-id="heading-4">window.onerror , error事件</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'error'</span>, <span class="hljs-built_in">this</span>.onError, <span class="hljs-literal">true</span>);
    <span class="hljs-built_in">window</span>.onerror = <span class="hljs-built_in">this</span>.onError
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>window.addEventListener('error')</code> 这种可以比 <code>window.onerror</code> 多捕获资源记载异常.
请注意最后一个参数是 <code>true</code>, <code>false</code>的话可能就不如你期望。</p>
<p>当然你如果问题这第三个参数的含义，我就有点不想理你了。拜。</p>
<h3 data-id="heading-5">unhandledrejection</h3>
<p>请注意最后一个参数是 <code>true</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.removeEventListener(<span class="hljs-string">'unhandledrejection'</span>, <span class="hljs-built_in">this</span>.onReject, <span class="hljs-literal">true</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其捕获未被捕获的Promise的异常。</p>
<h3 data-id="heading-6">XMLHttpRequest 与 fetch</h3>
<p><code>XMLHttpRequest</code> 很好处理，自己有onerror事件。
当然你99.99%也不会自己基于<code>XMLHttpRequest</code>封装一个库， <code>axios</code> 真香，有这完毕的错误处理机制。</p>
<p>至于<code>fetch</code>, 自己带着catch跑，不处理就是你自己的问题了。</p>
<p>这么多，太难了。<br>
还好，其实有一个库 <a href="https://www.npmjs.com/package/react-error-catch" target="_blank" rel="nofollow noopener noreferrer">react-error-catch</a> 是基于ErrorBoudary,error与unhandledrejection封装的一个组件。</p>
<p>其核心如下</p>
<pre><code class="hljs language-js copyable" lang="js">   ErrorBoundary.prototype.componentDidMount = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">// event catch</span>
        <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'error'</span>, <span class="hljs-built_in">this</span>.catchError, <span class="hljs-literal">true</span>);
        <span class="hljs-comment">// async code</span>
        <span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'unhandledrejection'</span>, <span class="hljs-built_in">this</span>.catchRejectEvent, <span class="hljs-literal">true</span>);
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> ErrorCatch <span class="hljs-keyword">from</span> <span class="hljs-string">'react-error-catch'</span>

<span class="hljs-keyword">const</span> App = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ErrorCatch</span>
      <span class="hljs-attr">app</span>=<span class="hljs-string">"react-catch"</span>
      <span class="hljs-attr">user</span>=<span class="hljs-string">"cxyuns"</span>
      <span class="hljs-attr">delay</span>=<span class="hljs-string">&#123;5000&#125;</span>
      <span class="hljs-attr">max</span>=<span class="hljs-string">&#123;1&#125;</span>
      <span class="hljs-attr">filters</span>=<span class="hljs-string">&#123;[]&#125;</span>
      <span class="hljs-attr">onCatch</span>=<span class="hljs-string">&#123;(errors)</span> =></span> &#123;
        console.log('报错咯');
        // 上报异常信息到后端，动态创建标签方式
        new Image().src = `http://localhost:3000/log/report?info=$&#123;JSON.stringify(errors)&#125;`
      &#125;&#125;
    >
      <span class="hljs-tag"><<span class="hljs-name">Main</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">ErrorCatch</span>></span></span>)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>鼓掌，鼓掌。</p>
<p>其实不然： 利用error捕获的错误，其最主要的是提供了错误堆栈信息，对于分析错误相当不友好，尤其打包之后。</p>
<p>错误那么多，我就先好好处理React里面的事件处理程序。<br>
至于其他，待续。</p>
<h2 data-id="heading-7">事件处理程序的异常捕获</h2>
<h3 data-id="heading-8">示例</h3>
<p>我的思路原理很简单，使用<a href="http://es6.ruanyifeng.com/#docs/decorator" target="_blank" rel="nofollow noopener noreferrer">decorator</a>来重写原来的方法。</p>
<p>先看一下使用：</p>
<pre><code class="hljs language-js copyable" lang="js">
   @methodCatch(&#123; <span class="hljs-attr">message</span>: <span class="hljs-string">"创建订单失败"</span>, <span class="hljs-attr">toast</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">report</span>:<span class="hljs-literal">true</span>, <span class="hljs-attr">log</span>:<span class="hljs-literal">true</span> &#125;)
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">createOrder</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> data = &#123;...&#125;;
        <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> createOrder();
        <span class="hljs-keyword">if</span> (!res || res.errCode !== <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">return</span> Toast.error(<span class="hljs-string">"创建订单失败"</span>);
        &#125;
        
        .......
        其他可能产生异常的代码
        .......
        
       Toast.success(<span class="hljs-string">"创建订单成功"</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意四个参数：</p>
<ul>
<li>message： 出现错误时，打印的错误</li>
<li>toast： 出现错误，是否Toast</li>
<li>report: 出现错误，是否上报</li>
<li>log: 使用使用console.error打印</li>
</ul>
<p>可能你说，这这，消息定死，不合理啊。我要是有其他消息呢。<br>
此时我微微一笑别急， 再看一段代码</p>
<pre><code class="hljs language-js copyable" lang="js">  @methodCatch(&#123; <span class="hljs-attr">message</span>: <span class="hljs-string">"创建订单失败"</span>, <span class="hljs-attr">toast</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">report</span>:<span class="hljs-literal">true</span>, <span class="hljs-attr">log</span>:<span class="hljs-literal">true</span> &#125;)
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">createOrder</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> data = &#123;...&#125;;
        <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> createOrder();
        <span class="hljs-keyword">if</span> (!res || res.errCode !== <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">return</span> Toast.error(<span class="hljs-string">"创建订单失败"</span>);
        &#125;
       
        .......
        其他可能产生异常的代码
        .......
        
       <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> CatchError(<span class="hljs-string">"创建订单失败了，请联系管理员"</span>, &#123;
           <span class="hljs-attr">toast</span>: <span class="hljs-literal">true</span>,
           <span class="hljs-attr">report</span>: <span class="hljs-literal">true</span>,
           <span class="hljs-attr">log</span>: <span class="hljs-literal">false</span>
       &#125;)
       
       Toast.success(<span class="hljs-string">"创建订单成功"</span>);

    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是都，没错，你可以通过抛出 自定义的<code>CatchError</code>来覆盖之前的默认选项。</p>
<p>这个<code>methodCatch</code>可以捕获，同步和异步的错误，我们来一起看看全部的代码。</p>
<h3 data-id="heading-9">类型定义</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> CatchOptions &#123;
    report?: <span class="hljs-built_in">boolean</span>;
    message?: <span class="hljs-built_in">string</span>;
    log?: <span class="hljs-built_in">boolean</span>;
    toast?: <span class="hljs-built_in">boolean</span>;
&#125;

<span class="hljs-comment">// 这里写到 const.ts更合理</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> DEFAULT_ERROR_CATCH_OPTIONS: CatchOptions = &#123;
    <span class="hljs-attr">report</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">"未知异常"</span>,
    <span class="hljs-attr">log</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">toast</span>: <span class="hljs-literal">false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">自定义的CatchError</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; CatchOptions, DEFAULT_ERROR_CATCH_OPTIONS &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@typess/errorCatch"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CatchError</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Error</span> </span>&#123;

    <span class="hljs-keyword">public</span> __type__ = <span class="hljs-string">"__CATCH_ERROR__"</span>;
    <span class="hljs-comment">/**
     * 捕捉到的错误
     * <span class="hljs-doctag">@param </span>message 消息
     * <span class="hljs-doctag">@options </span>其他参数
     */</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">message: <span class="hljs-built_in">string</span>, <span class="hljs-keyword">public</span> options: CatchOptions = DEFAULT_ERROR_CATCH_OPTIONS</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(message);
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">装饰器</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> Toast <span class="hljs-keyword">from</span> <span class="hljs-string">"@components/Toast"</span>;
<span class="hljs-keyword">import</span> &#123; CatchOptions, DEFAULT_ERROR_CATCH_OPTIONS &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@typess/errorCatch"</span>;
<span class="hljs-keyword">import</span> &#123; CatchError &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@util/error/CatchError"</span>;


<span class="hljs-keyword">const</span> W_TYPES = [<span class="hljs-string">"string"</span>, <span class="hljs-string">"object"</span>];
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">methodCatch</span>(<span class="hljs-params">options: <span class="hljs-built_in">string</span> | CatchOptions = DEFAULT_ERROR_CATCH_OPTIONS</span>) </span>&#123;

    <span class="hljs-keyword">const</span> <span class="hljs-keyword">type</span> = <span class="hljs-keyword">typeof</span> options;

    <span class="hljs-keyword">let</span> opt: CatchOptions;

    
    <span class="hljs-keyword">if</span> (options == <span class="hljs-literal">null</span> || !W_TYPES.includes(<span class="hljs-keyword">type</span>)) &#123; <span class="hljs-comment">// null 或者 不是字符串或者对象</span>
        opt = DEFAULT_ERROR_CATCH_OPTIONS;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> options === <span class="hljs-string">"string"</span>) &#123;  <span class="hljs-comment">// 字符串</span>
        opt = &#123;
            ...DEFAULT_ERROR_CATCH_OPTIONS,
            <span class="hljs-attr">message</span>: options || DEFAULT_ERROR_CATCH_OPTIONS.message,
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 有效的对象</span>
        opt = &#123; ...DEFAULT_ERROR_CATCH_OPTIONS, ...options &#125;
    &#125;

    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_target: <span class="hljs-built_in">any</span>, _name: <span class="hljs-built_in">string</span>, descriptor: PropertyDescriptor</span>): <span class="hljs-title">any</span> </span>&#123;

        <span class="hljs-keyword">const</span> oldFn = descriptor.value;

        <span class="hljs-built_in">Object</span>.defineProperty(descriptor, <span class="hljs-string">"value"</span>, &#123;
            <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxy</span>(<span class="hljs-params">...args: <span class="hljs-built_in">any</span>[]</span>) </span>&#123;
                    <span class="hljs-keyword">try</span> &#123;
                        <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> oldFn.apply(<span class="hljs-built_in">this</span>, args);
                        <span class="hljs-keyword">return</span> res;
                    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                        <span class="hljs-comment">// if (err instanceof CatchError) &#123;</span>
                        <span class="hljs-keyword">if</span>(err.__type__ == <span class="hljs-string">"__CATCH_ERROR__"</span>)&#123;
                            err = err <span class="hljs-keyword">as</span> CatchError;
                            <span class="hljs-keyword">const</span> mOpt = &#123; ...opt, ...(err.options || &#123;&#125;) &#125;;

                            <span class="hljs-keyword">if</span> (mOpt.log) &#123;
                                <span class="hljs-built_in">console</span>.error(<span class="hljs-string">"asyncMethodCatch:"</span>, mOpt.message || err.message , err);
                            &#125;

                            <span class="hljs-keyword">if</span> (mOpt.report) &#123;
                                <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span>:</span>
                            &#125;

                            <span class="hljs-keyword">if</span> (mOpt.toast) &#123;
                                Toast.error(mOpt.message);
                            &#125;

                        &#125; <span class="hljs-keyword">else</span> &#123;
                            
                            <span class="hljs-keyword">const</span> message = err.message || opt.message;
                            <span class="hljs-built_in">console</span>.error(<span class="hljs-string">"asyncMethodCatch:"</span>, message, err);

                            <span class="hljs-keyword">if</span> (opt.toast) &#123;
                                Toast.error(message);
                            &#125;
                        &#125;
                    &#125;
                &#125;
                proxy._bound = <span class="hljs-literal">true</span>;
                <span class="hljs-keyword">return</span> proxy;
            &#125;
        &#125;)
        <span class="hljs-keyword">return</span> descriptor;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">总结一下</h2>
<ol>
<li>利用装饰器重写原方法，达到捕获错误的目的</li>
<li>自定义错误类，抛出它，就能达到覆盖默认选项的目的。增加了灵活性。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">  @methodCatch(&#123; <span class="hljs-attr">message</span>: <span class="hljs-string">"创建订单失败"</span>, <span class="hljs-attr">toast</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">report</span>:<span class="hljs-literal">true</span>, <span class="hljs-attr">log</span>:<span class="hljs-literal">true</span> &#125;)
    <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">createOrder</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> data = &#123;...&#125;;
        <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> createOrder();
        <span class="hljs-keyword">if</span> (!res || res.errCode !== <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">return</span> Toast.error(<span class="hljs-string">"创建订单失败"</span>);
        &#125;
       Toast.success(<span class="hljs-string">"创建订单成功"</span>);
       
        .......
        其他可能产生异常的代码
        .......
        
       <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> CatchError(<span class="hljs-string">"创建订单失败了，请联系管理员"</span>, &#123;
           <span class="hljs-attr">toast</span>: <span class="hljs-literal">true</span>,
           <span class="hljs-attr">report</span>: <span class="hljs-literal">true</span>,
           <span class="hljs-attr">log</span>: <span class="hljs-literal">false</span>
       &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">下一步</h2>
<p>啥下一步，走一步看一步啦。</p>
<p>不，接下来的路，还很长。  这才是一个基础版本。</p>
<ol>
<li>扩大成果</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-meta">@XXXCatch</span>
classs AAA&#123;
    <span class="hljs-meta">@YYYCatch</span>
    method = <span class="hljs-function">()=></span> &#123;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>抽象，再抽象，再抽象</li>
</ol>
<p>再见。</p>
<h2 data-id="heading-14">写在最后</h2>
<p>写作不易，如果觉得还不错， 一赞一评，就是我最大的动力。</p>
<blockquote>
<p><a href="https://reactjs.org/docs/error-boundaries.html" target="_blank" rel="nofollow noopener noreferrer">error-boundaries</a><br>
<a href="https://www.colabug.com/1867349.html" target="_blank" rel="nofollow noopener noreferrer">React异常处理</a><br>
<a href="https://engineering.classdojo.com/blog/2016/12/10/catching-react-errors/" target="_blank" rel="nofollow noopener noreferrer">catching-react-errors</a><br>
<a href="https://blog.csdn.net/a986597353/article/details/78469979" target="_blank" rel="nofollow noopener noreferrer">react进阶之异常处理机制-error Boundaries</a><br>
<a href="http://es6.ruanyifeng.com/#docs/decorator" target="_blank" rel="nofollow noopener noreferrer">decorator</a><br>
<a href="https://github.com/jayphelps/core-decorators" target="_blank" rel="nofollow noopener noreferrer">core-decorators</a><br>
<a href="https://github.com/jayphelps/core-decorators/blob/master/src/autobind.js" target="_blank" rel="nofollow noopener noreferrer">autobind.js</a></p>
</blockquote></div>  
</div>
            