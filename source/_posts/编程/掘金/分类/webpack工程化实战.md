
---
title: 'webpack工程化实战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1405'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 03:28:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=1405'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAdCAYAAABcz8ldAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAhgSURBVGhD7Zp7bBTHHcdn33t7vvOdzy+ITVKDU0xIKG2ABCPTRCCaUiEVKWoqRJuASAhCitRCVKSoalFUKZBiSmmFRRJKRUnUtIpo+aNqGgwoOCmuFUIRzxjwE4zte+97drYzztji8HPvtkit/PnH+n1397Tz+83vN/PbMZhmmmmm+d+BoX8n5diihcGqgFQf5vk6BMAskWUlw3GyFnIvtqWSf91w7mKC3npfOLX7wYeiIa6BBWCOLLFRF2NB0JvIOP/80YG+k2ev6S699b/OzOfKBW5l5KsgyC4DCFQDnpEAdE1goc/dlNPc/Up7P711UiYNSMuyxeUzZPnHgGHWh5XADEkSAcdiN+AnEXIBhBComgFU0/xQR+jnj51sOUMf9Z0NKyL8S9+JPBEN8zuCMrsqGOA5QWAAyzLAxe53HBeYFgJp1c5Cx33nyIfpV3e+22/Sx32nev/sMCgVnmM4bjOniAtZWQAsz315EfsGQQc4hgWcjHkCmOj1rheuNn95cXwmDMiVp5etC/D8m5FwUWVQUYYGPh6mZYFUOgsGVa1pXvOZzVT2jRuH54RM230jEuI3RcIiL4l4UkxAJmuD/riVsqD7ct2m9nep7BtVTbVfZ0uE/UIk+CQflAHDjf8+Lg6MldYATGpH3c/Ul7p3dWXppVGM6eElJSHmnQWPbSlRlN1lJcUBjqNRnwJZVQO3B5P/uq5rK1d90pakckFcaKp5UJHY92JR8YlwkUDVySEZfGfQdO7E7Z8s2HL9TSoXTPXRud9nA8IBqSwcZgWeqpPj6BYw7yTbXBN9q2v9lQEq5zBmWA8vWLCptCi4tzwW8RQMQlFQATPLSh6vCSh/plJBkMyQBHZfWYnkKRgEktEVpTJXERN2Xzo4ex2VC6K6qXYpF5b3ypVRT8EgcAERSJXRbwCBOTFzXblM5RxGBaRt+ZPYA+LO0mgxz5K1Ig+UgAzKIuGnz39z6S+olDeaibaXRsU1RUFvgx+GwTWgPCaDgMw2XXpr9gwq50XV0bkxJiYeEiNF5cwE5XsiOEkAUkXkUW51SSOVchjl8WKef604XFSRbzCGCYeCoESStv/p8QU1VPIM3knNDynctnBRfsEYhgSlNCIGgQv2UCkvGIHZgteMh1nBW9W4F16RAM6yDVV7amZTaYQcr59cuuhhWRTWBvAMLxQGeyFSHOLnh0MvUskz5RF+fbRYDEy0mZgqQYUHOLhr//b6rGoqeaLqQG0pw3PrBbyA+4EQUkRmhvgqNUfICUipKK4OKUqIJVPKB0jpEhjmWWp64jdbKmVZZNYogcJm493gsifOqhDyeh9GYR/FM7sW+DA5CKR0MSK3tvKZkpwB5gRE4tjFEr7RL0iWBGV51vHFCyupNGWWPqLgnoer9mtyEGSJAzwLllDTGzyznDjRN/CwOFkoFb4bm0eVIXICgpvdGoEvrF7fC89zfLkkeV5HbOhWiTwTpKYvCAJLGshRdXtKMKAWlyxq+MPQLk1h66g5RE5ABJYNFrqY3wvJklJRUKg5ZWLFXIA86yek2uDOPkBNb3CM5Pf7DL2QyIrUGiLH+xC5Bmmm/ARnHUhC6PnzxWDK0RH5HuIjZGy27erU9AZ0dTIWXyG+NpBBrSFySxZw220IqeUPFoS6jVAPNadM7yDsgNB1qOkLuAziMYIb1PQGA75wIaKGPyAb+9oF16g5RE5ALIQ+tSyLWoWDEAK6aXW3JlK9VJoyx1oyvVkNdvo5KXXDAVkdnaKmNwx0xjH98w3JNmTCm+Bc9hKVhsgJSI9pvp9Vdd++jmq6AXB2/HHrhcs5aTkVDv0DFzoHvKdq/mQsKX/4t7KJLDpOJW+IbAvMGoMkxfwAWZB8DT7W1diTE+WcgKz6pK1bs6z3daPwmJDsSKt6ZsCyjlLJMz0DsDGZ8SdlDROBjOb8YeWOjptU8kTXusuaazu7oJrfEnQvdkpVcUn6PTVHyAkIIW7br/Unklni0EJIZ1WgGsauZR+fvUglz6zY0dGfVp09ybRNlfwgi3k8YSbvJJ29VMoLt9v6rZVQL7hOYUubndHJGclBtzn1byqNMCogi09/2nFb01/oj+f/5TyjauBOKtPcZ1r7qZQ3f2lRfxZPWi2anp8TSDAGExZMa2jr8u03L1M5L7q3Xc+iAeuHRl/ScvPcjSLDBnZS/cjtNHd2v3171Ewbs9N5q7Pn4otVMx3btBsCsoRbk1FxG5dMVgMDqfTpXl1/tuFMa5zKefPROdX59qLQBwLnNog8Wy1OcjB1N+QEsW/QsFNZuO35Xb1v98QLX4/Sx+O3wqujrQ6013ABUWI8+AaqBjAH01+ghL22+5X2PirnMG7r+esbnae/V1neauvGSoHjigTcVU7UGFm2DeK4ttxKpQ+mLPvl+o/PjnkAkw9HTqSMmVHhyAMx9iFcSh/BHTfLceO/C8mKjApBf9zszGhoY92m9sN+BGOY9AeD7eGniv8OTaOB4dgyTsQd9wS+IQu4lciYdkI7CLrNH3Rvbb9FL41i0tbzVP2iWJkobpN5fmM4IJfJskTP1Bk8A9HQmbpmGDBrWqdVCN/Yd7PjxKGOXn+bmbto3feVVcVB9qehIL8EJy8nChwgr0O2xxBnhGU5eP2CfYbl/m4gBRsbtneMORP9oGpjpcCsiKzHHfdOPiQ/wMniyFEu2dbiTQCAeN/vavC466BGYLttXc9fmXBXMGlAhiHHur+sq6uPiUI9z7CVHMPwBnLSuuN8FuC48/Oaz1ylt94XfrW5ouyprwWfYRkwNyCyYYjwkBHows1fa+tV/fzGxlv39b9gqvfPmQ+i/HK8KlcBjhHwfl8HEHyOd1JnuzZd66S3TTPNNNP8/wDAfwDG7G0m9LKBpwAAAABJRU5ErkJggg==) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">项目准备</h2>
<p>完整配置代码已上传至github，仅供参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FTimorCookie%2Fwebpack4.x" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/TimorCookie/webpack4.x" ref="nofollow noopener noreferrer">github.com/TimorCookie…</a></p>
<h3 data-id="heading-1">初始化</h3>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 初始化 npm 配置文件</span>
npm init -y 
<span class="hljs-comment"># 安装核心库和命令行工具</span>
npm install webpack@4.44.0 webpack-cli@3.3.12 --save-dev 

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">.npmrc</h3>
<p>在为了解决npm龟速下载的糟糕体验时，我们一般会将npm源设置为淘宝镜像源</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm config <span class="hljs-built_in">set</span> registry https://registry.npm.taobao.org
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是大家想想，万一某个同学克隆了你的项目之后，准备在他本地开发的时候，并没有设置淘宝镜像 源，又要人家去手动设置一遍，我们作为项目的发起者，就先给别人省下这份时间吧，只需要在根目录 添加一个 .npmrc 并做简单的配置即可:</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 根目录下创建 .npmrc 文件</span>
touch .npmrc

<span class="hljs-comment"># 在该文件内输入配置</span>
registry=https://registry.npm.taobao.org/

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">创建webpack配置文件</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'./dist'</span>)
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">样式处理</h3>
<h4 data-id="heading-5">集成 css 样式处理</h4>
<ul>
<li>安装 (style-loader 需要安装2.x版本）</li>
</ul>
<pre><code class="hljs language-bash copyable" lang="bash">npm install css-loader style-loader@2 --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>配置</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'./dist'</span>)
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>]
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">集成 less / sass</h4>
<ul>
<li>
<p>安装 sass 和 less 相关模块( less-loader 安装7.x版本，sass-loader 安装10.x版本)</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment">#less</span>
npm install less less-loader@7 --save-dev

<span class="hljs-comment">#sass</span>
npm install node-sass sass-loader@10 --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'./dist'</span>)
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.less$/</span>,
        use: [<span class="hljs-string">"style-loader"</span>, <span class="hljs-string">"css-loader"</span>, <span class="hljs-string">"less-loader"</span>]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.scss/</span>,
        use: [<span class="hljs-string">"style-loader"</span>, <span class="hljs-string">"css-loader"</span>, <span class="hljs-string">"sass-loader"</span>]
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-7">集成 postcss</h4>
<p>Github:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpostcss%2Fpostcss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/postcss/postcss" ref="nofollow noopener noreferrer">github.com/postcss/pos…</a></p>
<p><em><strong>postcss之于css 相当于babel之于js</strong></em></p>
<p>postcss主要功能只有两个:</p>
<ol>
<li>
<p>把css解析成JS可以操作的抽象语法树AST，</p>
</li>
<li>
<p>第二就是调用插 件来处理AST并得到结果;</p>
</li>
</ol>
<p>所以postcss一般都是通过插件来处理css，并不会直接处理 比如：autoprefixer（自动补⻬浏览器前缀）  cssnano（css压缩）</p>
<ul>
<li>
<p>安装（postcss-loader 需要安装6.x版本）</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install postcss-loader@6 autoprefixer cssnano --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>配置<code>postcss.config.js</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># postcss.config.js
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [<span class="hljs-built_in">require</span>(<span class="hljs-string">'autoprefixer'</span>), <span class="hljs-built_in">require</span>(<span class="hljs-string">'cssnano'</span>)]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>配置浏览器兼容版本</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># 配置package.json
<span class="hljs-string">"browserslist"</span>:[<span class="hljs-string">"last 2 versions"</span>, <span class="hljs-string">"> 1%"</span>],
  
# 或者直接在postcss.config.js里配置 <span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-built_in">require</span>(<span class="hljs-string">"autoprefixer"</span>)(&#123;
      <span class="hljs-attr">overrideBrowserslist</span>: [<span class="hljs-string">"last 2 versions"</span>, <span class="hljs-string">"> 1%"</span>],
    &#125;),
], &#125;;

# 或者创建.browserslistrc文件 
> <span class="hljs-number">1</span>%
last <span class="hljs-number">2</span> versions
not ie <= <span class="hljs-number">8</span>
 
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>配置<code>webpack.config.js</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'./dist'</span>)
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'postcss-loader'</span>]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.less$/</span>,
        use: [<span class="hljs-string">"style-loader"</span>, <span class="hljs-string">"css-loader"</span>, <span class="hljs-string">"postcss-loader"</span>]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.scss/</span>,
        use: [<span class="hljs-string">"style-loader"</span>, <span class="hljs-string">"css-loader"</span>, <span class="hljs-string">"postcss-loader"</span>]
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-8">样式分离</h4>
<p>经过如上几个loader处理，css最终是打包在js中的，运行时会动态插入head中，但是我们一般在生产环 境会把css文件分离出来(有利于用户端缓存、并行加载及减小js包的大小)，这时候就用到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwebpack-contrib%2Fmini-css-extract-plugin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/webpack-contrib/mini-css-extract-plugin" ref="nofollow noopener noreferrer">mini-css- extract-plugin</a> 插件。</p>
<ul>
<li>
<p>安装(需要安装1.x版本)</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install mini-css-extract-plugin@1 -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'./dist'</span>)
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// MiniCssExtractPlugin 需要参与模块解析，须在此设置此项，不再需要style-loader</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'postcss-loader'</span>]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.less$/</span>,
        use: [MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader, '</span>postcss-loader<span class="hljs-string">']
      &#125;,
      &#123;
        test:/\.scss/,
        use: [MiniCssExtractPlugin.loader, '</span>css-loader<span class="hljs-string">', '</span>postcss-loader<span class="hljs-string">']
      &#125;
    ]
  &#125;,
  plugins: [new MiniCssExtractPlugin(&#123;
    filename: [name].css,
    ...
  &#125;)]
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-9">图片 / 字体文件处理</h3>
<p><code>url-loader</code> 和 <code>file-loader</code> 都可以用来处理本地的资源文件，如图片、字体、音视频等。功能也是 类似的， 不过<code>url-loader</code> 可以指定在文件大小小于指定的限制时，返回 DataURL ，不会输出真实的 文件，可以减少昂贵的网络请求。</p>
<ul>
<li>
<p>安装（使用url-loader 必须要 安装 file-loader）</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install url-loader file-loader --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'./dist'</span>)
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// MiniCssExtractPlugin 需要参与模块解析，须在此设置此项，不再需要style-loader</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'postcss-loader'</span>]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.less$/</span>,
        use: [MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader, '</span>postcss-loader<span class="hljs-string">']
      &#125;,
      &#123;
        test:/\.scss/,
        use: [MiniCssExtractPlugin.loader, '</span>css-loader<span class="hljs-string">', '</span>postcss-loader<span class="hljs-string">']
      &#125;,
      &#123;
test: /\.(png|jpg|gif|jpeg|webp|svg|eot|ttf|woff|woff2)$/,
        use: [
          &#123;
            // 仅配置 url-loader 就行，内部会自动调用 file-loader
            loader: '</span>url-loader<span class="hljs-string">', 
            options: &#123;
              limit: 10240,
              name: '</span>[name]_[hash:<span class="hljs-number">6</span>].[ext]<span class="hljs-string">',
              outputPath: '</span>assets<span class="hljs-string">' // 设置资源输出目录
            &#125;
          &#125;
        ]
      &#125;
    ]
  &#125;,
  plugins: [new MiniCssExtractPlugin(&#123;
    filename: [name].css,
    ...
  &#125;)]
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意:</strong></p>
<p>limit的设置要设置合理，太大会导致JS文件加载变慢，需要兼顾加载速度和网络请求次数。 如果需要使用图片压缩功能，可以使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftcoopman%2Fimage-webpack-loader" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tcoopman/image-webpack-loader" ref="nofollow noopener noreferrer">image-webpack-loader</a></p>
<p><strong>webpack文件指纹策略:</strong></p>
<ul>
<li>
<p>hash策略 是以项目为单位的，项目内容改变，则会生成新的hash,内容不变则hash不变</p>
</li>
<li>
<p>chunkhash 以chunk为单位，当一个文件内容改变，则整个chunk组的模块hash都会改变</p>
</li>
<li>
<p>contenthash 以自身内容为单位</p>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-10">HMTL 页面处理</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjantimon%2Fhtml-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jantimon/html-webpack-plugin" ref="nofollow noopener noreferrer">htmlwebpackplugin</a>会在打包结束后，自动生成一个 html 文件，并把打包生成的 js 模块引入到该 html 中。</p>
<ul>
<li>
<p>安装</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i html-webpack-plugin@4 --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>参数列表</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> 
<span class="hljs-attr">title</span>: 用来生成⻚面的 title 元素
<span class="hljs-attr">filename</span>: 输出的 HTML 文件名，默认是 index.html, 也可以直接配置带有子目录。
<span class="hljs-attr">template</span>: 模板文件路径，支持加载器，比如 html!./index.html
<span class="hljs-attr">inject</span>: <span class="hljs-literal">true</span> | <span class="hljs-string">'head'</span> | <span class="hljs-string">'body'</span> | <span class="hljs-literal">false</span> ,注入所有的资源到特定的 template 或者 templateContent 中，如果设置为 <span class="hljs-literal">true</span> 或者 body，所有的 javascript 资源将被放置到 body 元素的底部，<span class="hljs-string">'head'</span> 将放置到 head 元素中。
<span class="hljs-attr">favicon</span>: 添加特定的 favicon 路径到输出的 HTML 文件中。
<span class="hljs-attr">minify</span>: &#123;&#125; | <span class="hljs-literal">false</span> , 传递 html-minifier 选项给 minify 输出
<span class="hljs-attr">hash</span>: <span class="hljs-literal">true</span> | <span class="hljs-literal">false</span>, 如果为 <span class="hljs-literal">true</span>, 将添加一个唯一的 webpack 编译 hash 到所有包含的脚本和 CSS 文件，对于解除 cache 很有用。
<span class="hljs-attr">cache</span>: <span class="hljs-literal">true</span> | <span class="hljs-literal">false</span>，如果为 <span class="hljs-literal">true</span>, 这是默认值，仅仅在文件修改之后才会发布文件。 showErrors: <span class="hljs-literal">true</span> | <span class="hljs-literal">false</span>, 如果为 <span class="hljs-literal">true</span>, 这是默认值，错误信息会写入到 HTML ⻚面中 chunks: 允许只添加某些块 (比如，仅仅 unit test 块)
<span class="hljs-attr">chunksSortMode</span>: 允许控制块在添加到⻚面之前的排序方式，支持的值:<span class="hljs-string">'none'</span> | <span class="hljs-string">'default'</span> | &#123;<span class="hljs-function"><span class="hljs-keyword">function</span>&#125;-<span class="hljs-title">default</span>:'<span class="hljs-title">auto</span>'
<span class="hljs-title">excludeChunks</span>: 允许跳过某些块，(<span class="hljs-params">比如，跳过单元测试的块</span>)
 
</span><span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>配置</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js 
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);
<span class="hljs-keyword">const</span> htmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"html-webpack-plugin"</span>);
<span class="hljs-built_in">module</span>.exports = &#123;
 ...
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> htmlWebpackPlugin(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">"My App"</span>,
      <span class="hljs-attr">filename</span>: <span class="hljs-string">"app.html"</span>,
      <span class="hljs-attr">template</span>: <span class="hljs-string">"./src/index.html"</span>
&#125;) ]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-11">打包文件清理</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjohnagan%2Fclean-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/johnagan/clean-webpack-plugin" ref="nofollow noopener noreferrer">clean-webpack-plugin</a>这个插件是用来帮我们清除打包之后 dist 目录下的其他多余或者无用的代码，因为我们之前可能生成过其他的代码，如果不清楚的话可能多个代码掺杂在一起容易把我们搞混乱了<code>clean-webpack-plugin</code> 插件 就是这样由来的。每次生成代码之前先将 dist 目录清空</p>
<ul>
<li>
<p>安装</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install clean-webpack-plugin --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js 
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">"path"</span>);
<span class="hljs-keyword">const</span> htmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"html-webpack-plugin"</span>);
<span class="hljs-keyword">const</span> <span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"clean-webpack-plugin"</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
 ...
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> htmlWebpackPlugin(&#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">"My App"</span>,
      <span class="hljs-attr">filename</span>: <span class="hljs-string">"app.html"</span>,
      <span class="hljs-attr">template</span>: <span class="hljs-string">"./src/index.html"</span>
&#125;),
    <span class="hljs-keyword">new</span> CleanWebpackPlugin(&#123;&#125;)
  ]
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Q：clean-webpack-plugin:如何做到dist目录下某个文件或目录不被清空？</strong></p>
<p>A：使用配置 项:cleanOnceBeforeBuildPatterns 案例:cleanOnceBeforeBuildPatterns: ["<strong>/*", "!dll", "!dll/</strong>"], !感 叹号相当于exclude 排除，意思是清空操作排除dll目录，和dll目录下所有文件。 注意:数组列表里的 “**/*”是默认值，不可忽略，否则不做清空操作。</p>
</li>
</ul>
<h3 data-id="heading-12">sourceMap</h3>
<p>源代码与打包后的代码的映射关系，通过<code>sourceMap</code>定位到源代码。 在dev模式中，默认开启，关闭的话 可以在配置文件里配置<code>devtool:"none"</code></p>
<p>devtool的介绍:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Fconfiguration%2Fdevtool%23devtool" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/configuration/devtool#devtool" ref="nofollow noopener noreferrer">webpack.js.org/configurati…</a></p>
<ul>
<li>eval：速度最快,使用<code>eval</code>包裹模块代码,</li>
<li>source-map：产生 <code>.map</code> 文件</li>
<li>cheap：较快，不包含列信息</li>
<li>Module：第三方模块，包含 <code>loader</code> 的 sourcemap (比如<code>jsx to js</code> ，<code>babel</code> 的 sourcemap)</li>
<li>inline: 将<code>.map</code>作为DataURI嵌入，不单独生成 <code>.map </code>文件</li>
</ul>
<p>配置推荐</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> devtool:<span class="hljs-string">"cheap-module-eval-source-map"</span>,<span class="hljs-comment">// 开发环境配置</span>
<span class="hljs-comment">//线上不推荐开启</span>
<span class="hljs-attr">devtool</span>:<span class="hljs-string">"cheap-module-source-map"</span>, <span class="hljs-comment">// 线上生成配置</span>
 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">配置开发服务器</h3>
<p>每次改完代码都需要重新打包一次，打开浏览器，刷新一次，很麻烦，我们可以安装使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconfiguration%2Fdev-server%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/configuration/dev-server/" ref="nofollow noopener noreferrer">webpackdevserver</a>来改善这块的体验</p>
<ul>
<li>
<p>安装</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install webpack-dev-server@3.11.0 --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>配置</p>
<ul>
<li>package.json</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json">
&#123;
  ...
  <span class="hljs-attr">"script"</span>: &#123;
    ...
    <span class="hljs-attr">"server"</span>: <span class="hljs-string">"webpack-dev-server"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Web pack.config.js</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> MiniCssExtractPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mini-css-extract-plugin'</span>);
<span class="hljs-keyword">const</span> htmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"html-webpack-plugin"</span>);
<span class="hljs-keyword">const</span> <span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"clean-webpack-plugin"</span>)
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'./dist'</span>)
  &#125;,
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">contentBase</span>: <span class="hljs-string">"./dist"</span>,
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">port</span>: <span class="hljs-number">8080</span>
  &#125;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// MiniCssExtractPlugin 需要参与模块解析，须在此设置此项，不再需要style-loader</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'postcss-loader'</span>]
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>:<span class="hljs-regexp">/\.less$/</span>,
        use: [MiniCssExtractPlugin.loader, <span class="hljs-string">'css-loader, '</span>postcss-loader<span class="hljs-string">']
      &#125;,
      &#123;
        test:/\.scss/,
        use: [MiniCssExtractPlugin.loader, '</span>css-loader<span class="hljs-string">', '</span>postcss-loader<span class="hljs-string">']
      &#125;,
      &#123;
test: /\.(png|jpg|gif|jpeg|webp|svg|eot|ttf|woff|woff2)$/,
        use: [
          &#123;
            // 仅配置 url-loader 就行，内部会自动调用 file-loader
            loader: '</span>url-loader<span class="hljs-string">', 
            options: &#123;
              limit: 10240,
              name: '</span>[name]_[hash:<span class="hljs-number">6</span>].[ext]<span class="hljs-string">',
              outputPath: '</span>assets<span class="hljs-string">' // 设置资源输出目录
            &#125;
          &#125;
        ]
      &#125;
    ]
  &#125;,
  plugins: [
    new MiniCssExtractPlugin(&#123;
      filename: [name].css,
      ...
  &#125;),
    new htmlWebpackPlugin(&#123;
      title: "My App",
      filename: "app.html",
      template: "./src/index.html"
&#125;),
    new CleanWebpackPlugin(&#123;&#125;)
  ]
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>启动</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm run serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动服务后，会发现dist目录没有了，这是因为devServer把打包后的模块不会放在dist目录下，而是放 到内存中，从而提升速度</p>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-14">解决跨域</h3>
<p>联调期间，前后端分离，直接获取数据会跨域，上线后我们使用nginx转发，开发期间，webpack就可以搞定这件事</p>
<p>启动一个服务器，mock一个接口<code>npm i express -D</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建一个server.js 修改scripts "server":"node server.js"</span>
# server.js
<span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)
<span class="hljs-keyword">const</span> app = express()
app.get(<span class="hljs-string">'/api/info'</span>, <span class="hljs-function">(<span class="hljs-params">req,res</span>)=></span>&#123;
  res.json(&#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'Timokie'</span>,
    <span class="hljs-attr">age</span>:<span class="hljs-number">18</span>, 
    <span class="hljs-attr">msg</span>:<span class="hljs-string">'hello, Timokie!'</span>
  &#125;) 
&#125;)
app.listen(<span class="hljs-string">'9092'</span>)
<span class="hljs-comment">// node server.js</span>
<span class="hljs-comment">// http://localhost:9092/api/info</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>项目中安装axios工具<code>npm i axios -D</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># index.js
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
axios.get(<span class="hljs-string">'http://localhost:9092/api/info'</span>).then(<span class="hljs-function"><span class="hljs-params">res</span>=></span>&#123;
    <span class="hljs-built_in">console</span>.log(res)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>产生跨域问题，此时我们可以修改 <code>webpack.config.js</code> 来设置服务器代理</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports=&#123;
  ...
<span class="hljs-attr">proxy</span>: &#123;
    <span class="hljs-string">"/api"</span>: &#123;
      <span class="hljs-attr">target</span>: <span class="hljs-string">"http://localhost:9092"</span>
    &#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改<code>index.js</code>请求路径</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> axios.get(<span class="hljs-string">"/api/info"</span>).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(res);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">模块热替换</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconcepts%2Fhot-module-replacement%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/concepts/hot-module-replacement/" ref="nofollow noopener noreferrer">Hot Module Replacement</a>（**HMR:**模块热替换）</p>
<p>模块热替换(HMR - hot module replacement)功能会在应用程序运行过程中，替换、添加或删除 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconcepts%2Fmodules%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/concepts/modules/" ref="nofollow noopener noreferrer">模块</a>，而无需重新加载整个页面。主要是通过以下几种方式，来显著加快开发速度：</p>
<ul>
<li>保留在完全重新加载页面期间丢失的应用程序状态。</li>
<li>只更新变更内容，以节省宝贵的开发时间。</li>
<li>在源代码中 CSS/JS 产生修改时，会立刻在浏览器中进行更新，这几乎相当于在浏览器 devtools 直接更改样式。</li>
</ul>
<p><strong>启动hmr</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js
<span class="hljs-built_in">module</span>.exports = &#123;
  ...
 
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">contentBase</span>: <span class="hljs-string">"./dist"</span>,
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">hot</span>:<span class="hljs-literal">true</span>, <span class="hljs-comment">//即便HMR不生效，浏览器也不自动刷新，就开启hotOnly hotOnly:true</span>
  &#125;,
  
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>配置文件头部引入webpack</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js
<span class="hljs-comment">//const path = require("path");</span>
<span class="hljs-comment">// const MiniCssExtractPlugin = require('mini-css-extract-plugin');</span>
<span class="hljs-comment">//const HtmlWebpackPlugin = require("html-webpack-plugin");</span>
<span class="hljs-comment">//const CleanWebpackPlugin = require("clean-webpack-plugin");</span>
<span class="hljs-keyword">const</span> webpack = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>在插件配置处添加:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js
<span class="hljs-built_in">module</span>.exports = &#123;
  ...,
   
<span class="hljs-attr">plugins</span>: [
    <span class="hljs-keyword">new</span> CleanWebpackPlugin(),
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: <span class="hljs-string">"src/index.html"</span>
    &#125;),
    <span class="hljs-keyword">new</span> webpack.HotModuleReplacementPlugin()
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>案例</strong></p>
<ul>
<li>
<p>处理 css 模块 HMR</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> 
# index.js
<span class="hljs-keyword">import</span> <span class="hljs-string">"./css/index.css"</span>;
<span class="hljs-keyword">var</span> btn = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"button"</span>); 
btn.innerHTML = <span class="hljs-string">"新增"</span>; 
<span class="hljs-built_in">document</span>.body.appendChild(btn);
btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
  div.innerHTML = <span class="hljs-string">"item"</span>;
  <span class="hljs-built_in">document</span>.body.appendChild(div);
&#125;;

# index.css
<span class="hljs-attr">div</span>:nth-<span class="hljs-keyword">of</span>-<span class="hljs-function"><span class="hljs-title">type</span>(<span class="hljs-params">odd</span>)</span> &#123;
  <span class="hljs-attr">background</span>: yellow;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>处理 js 模块 HMR</p>
<p><strong>需要使用<code>module.hot.accept</code>来观察模块变更从而更新</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># counter.js
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">counter</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
  div.setAttribute(<span class="hljs-string">"id"</span>, <span class="hljs-string">"counter"</span>);
  div.innerHTML = <span class="hljs-number">1</span>;
  div.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    div.innerHTML = <span class="hljs-built_in">parseInt</span>(div.innerHTML, <span class="hljs-number">10</span>) + <span class="hljs-number">1</span>;
  &#125;;
  <span class="hljs-built_in">document</span>.body.appendChild(div);
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> counter;


# number.js
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">number</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
  div.setAttribute(<span class="hljs-string">"id"</span>, <span class="hljs-string">"number"</span>);
  div.innerHTML = <span class="hljs-number">13000</span>;
  <span class="hljs-built_in">document</span>.body.appendChild(div);
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> number;


# index.js
<span class="hljs-keyword">import</span> counter <span class="hljs-keyword">from</span> <span class="hljs-string">"./counter"</span>;
<span class="hljs-keyword">import</span> number <span class="hljs-keyword">from</span> <span class="hljs-string">"./number"</span>;
counter();
number();
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.hot) &#123;
  <span class="hljs-built_in">module</span>.hot.accept(<span class="hljs-string">"./b"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">document</span>.body.removeChild(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"number"</span>));
    number();
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-16">集成 Babel 处理 ES6</h3>
<p>官方网站：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbabeljs.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://babeljs.io/" ref="nofollow noopener noreferrer">babeljs.io/</a></p>
<p>中文网站：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.babeljs.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.babeljs.cn/" ref="nofollow noopener noreferrer">www.babeljs.cn/</a></p>
<p>Babel是 JavaScript 编译器，能将 ES6 代码转换成 ES5 代码，让我们开发过程中放心使用JS新特性而不用担心兼容性问题，并且还可以通过插件机制根据需求灵活的扩展。</p>
<p>Babel在执行编译的过程中，会从项目根目录下的<code>.babelrc</code> 的 JSON 文件中读取配置。没有该文件会从 loader 的 options 地方读取配置。</p>
<ul>
<li>
<p>安装 babel</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install @babel/core @babel/preset --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>babel-loader</code>是 webpack 与 babel 的通信桥梁，不会做把es6转成es5的工作，这部分工作需要用到<code>@babel/preset-env</code>来做</p>
<ul>
<li>
<p>es6+ ----->babel(presets-env)-----> es5</p>
</li>
<li>
<p>flow语法 ---->babel(presets-flow)->es5</p>
</li>
<li>
<p>jsx语法 ---->babel(preset-react) ->es5</p>
</li>
<li>
<p>ts语法 ---->babel(preset-ts) -->es5</p>
</li>
</ul>
</li>
<li>
<p>配置 webpack.config.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js
<span class="hljs-built_in">module</span>.exports = &#123;
  ...
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [  
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        use: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">"babel-loader"</span>,
          <span class="hljs-attr">options</span>: &#123;
            <span class="hljs-attr">presets</span>: [<span class="hljs-string">"@babel/preset-env"</span>]
          &#125;
       &#125;&#125;
     ]
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的几步 还不够，默认的 Babel 只支持 let 等一些基础的特性转换，Promise 等一些还有转换过 来，这时候需要借助<code>@babel/polyfill</code>，把 es 的新特性都装进来，来弥补低版本浏览器中缺失的特性</p>
</li>
<li>
<p>安装生产依赖 @babel/polyfill</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 注意： @babel/polyfill 是生产依赖</span>
npm install @babel-polyfill --save
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>修改入口文件，在顶部注入 polyfill</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># index.js
<span class="hljs-keyword">import</span> <span class="hljs-string">"@babel/polyfill"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>执行打包命令后，会发现打包的体积大了很多，这是因为polyfill默认会把所有特性注入进来，假如我想我用到的es6+，才 会注入，没用到的不注入，从而减少打包的体积，就需要配置按需加载，减少冗余</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"># webpack.config.js
# webpack.config.js
<span class="hljs-built_in">module</span>.exports = &#123;
  ...
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [  
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.js$/</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">"babel-loader"</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">presets</span>: [
                [
                  <span class="hljs-string">"@babel/preset-env"</span>,
                  &#123;
                    <span class="hljs-attr">targets</span>: &#123;
                      <span class="hljs-attr">edge</span>: <span class="hljs-string">"17"</span>,
                      <span class="hljs-attr">firefox</span>: <span class="hljs-string">"60"</span>,
                      <span class="hljs-attr">chrome</span>: <span class="hljs-string">"67"</span>,
                      <span class="hljs-attr">safari</span>: <span class="hljs-string">"11.1"</span>,
                    &#125;,
                    <span class="hljs-comment">//新版本需要指定核心库版本</span>
                    <span class="hljs-attr">corejs</span>: <span class="hljs-number">2</span>,
                    <span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">"entry"</span>,
                  &#125;,
                ],
              ],
            &#125;,
          &#125;,
        ],
      &#125;,
     ]
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>useBuiltIns</code> 选项是 babel 7 的新功能，这个选项告诉 babel 如何配置 @babel/polyfill 。</p>
<p>它有三 个参数可以使用:</p>
<ul>
<li>entry：需要在 webpack 的入口文件里 <code>import "@babel/polyfill" </code>一次。 babel 会根据你的使用情况导入垫片，没有使用的功能不会被导入相应的垫片。</li>
<li>usage：不需要 import ，全 自动检测，但是要安装 @babel/polyfill 。</li>
<li>false：如果你 <code>import "@babel/polyfill"</code> ，它不会排 除掉没有使用的垫片，程序体积会庞大。(不推荐)</li>
</ul>
<p>扩展:
babelrc文件: 新建.babelrc文件，把options部分移入到该文件中，就可以了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> 
#.babelrc
 &#123;
  <span class="hljs-attr">presets</span>: [
    [
      <span class="hljs-string">"@babel/preset-env"</span>,
      &#123;
        <span class="hljs-attr">targets</span>: &#123;
          <span class="hljs-attr">edge</span>: <span class="hljs-string">"17"</span>,
          <span class="hljs-attr">firefox</span>: <span class="hljs-string">"60"</span>,
          <span class="hljs-attr">chrome</span>: <span class="hljs-string">"67"</span>,
          <span class="hljs-attr">safari</span>: <span class="hljs-string">"11.1"</span>,
        &#125;,
        <span class="hljs-comment">//新版本需要指定核心库版本</span>
        <span class="hljs-attr">corejs</span>: <span class="hljs-number">2</span>,
        <span class="hljs-attr">useBuiltIns</span>: <span class="hljs-string">"entry"</span>,
      &#125;,
    ],
  ],
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            