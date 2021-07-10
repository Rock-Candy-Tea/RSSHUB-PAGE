
---
title: '【有趣的项目分享】尝试用AI合成特朗普的语音'
categories: 
 - 编程
 - 掘金
 - 单个收藏夹
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/898412f2b64d461fae7f074248a9cb27~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 14 Sep 2020 00:41:48 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/898412f2b64d461fae7f074248a9cb27~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这两天看到了一个项目<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FCorentinJ%2FReal-Time-Voice-Cloning" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/CorentinJ/Real-Time-Voice-Cloning" ref="nofollow noopener noreferrer">Real-Time-Voice-Cloning</a>，它可以通过一段声音的片段模拟一个人的声音。我感觉还是蛮有意思的。</p>
<p>这里有个作者的介绍视频可以看：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1W4411B7ge%3Ffrom%3Dsearch%26seid%3D13108021530641486286" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1W4411B7ge?from=search&seid=13108021530641486286" ref="nofollow noopener noreferrer">BV1W4411B7ge</a>。不过我觉得他给出的客户端软件不如直接上代码更直接。</p>
<p>这里我用特朗普的语音来举个例子。</p>
<h2 data-id="heading-0">环境搭建</h2>
<h3 data-id="heading-1">首先clone代码</h3>
<pre><code class="hljs language-bash copyable" lang="bash">git <span class="hljs-built_in">clone</span> https://github.com/CorentinJ/Real-Time-Voice-Cloning.git
<span class="hljs-built_in">cd</span> Real-Time-Voice-Cloning
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">安装依赖</h3>
<p>这里环境搭建比较简单，基本不会遇到坑，步骤如下：</p>
<ul>
<li>安装Python3.6 or Python3.7</li>
<li>安装ffmpeg</li>
<li>安装PyTorch (>=1.0.1)</li>
<li>最后通过pip安装依赖了：<code>pip3 install -r requirements.txt</code></li>
</ul>
<h3 data-id="heading-3">下载预训练的模型</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FCorentinJ%2FReal-Time-Voice-Cloning%2Fwiki%2FPretrained-models" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/CorentinJ/Real-Time-Voice-Cloning/wiki/Pretrained-models" ref="nofollow noopener noreferrer">github.com/CorentinJ/R…</a></p>
<p>这里有三个模型（encoder,synthesizer,vocoder）的参数，把save_models文件夹分别放入到对应的文件夹即可。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/898412f2b64d461fae7f074248a9cb27~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">准备音频数据</h2>
<p>这里为了模仿特朗普的声音，我从youtube上面找了一个特朗普的演讲，并截取了一小段，保存成一个文件。</p>
<h2 data-id="heading-5">生成语音</h2>
<p>接下来就可以生成语音了，这里建立一个jupyter notebook。</p>
<h3 data-id="heading-6">加载模型</h3>
<pre><code class="hljs language-python copyable" lang="python"><span class="hljs-comment"># 导入模型参数</span>
<span class="hljs-keyword">from</span> IPython.display <span class="hljs-keyword">import</span> Audio
<span class="hljs-keyword">from</span> IPython.utils <span class="hljs-keyword">import</span> io
<span class="hljs-keyword">from</span> synthesizer.inference <span class="hljs-keyword">import</span> Synthesizer
<span class="hljs-keyword">from</span> encoder <span class="hljs-keyword">import</span> inference <span class="hljs-keyword">as</span> encoder
<span class="hljs-keyword">from</span> vocoder <span class="hljs-keyword">import</span> inference <span class="hljs-keyword">as</span> vocoder
<span class="hljs-keyword">from</span> pathlib <span class="hljs-keyword">import</span> Path
<span class="hljs-keyword">import</span> numpy <span class="hljs-keyword">as</span> np
<span class="hljs-keyword">import</span> librosa
encoder_weights = Path(<span class="hljs-string">"encoder/saved_models/pretrained.pt"</span>)
vocoder_weights = Path(<span class="hljs-string">"vocoder/saved_models/pretrained/pretrained.pt"</span>)
syn_dir = Path(<span class="hljs-string">"synthesizer/saved_models/logs-pretrained/taco_pretrained"</span>)
encoder.load_model(encoder_weights)
synthesizer = Synthesizer(syn_dir)
vocoder.load_model(vocoder_weights)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">调用模型并生成语音</h3>
<pre><code class="hljs language-python copyable" lang="python"><span class="hljs-comment">#@title Deep vocoder</span>
<span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">synth</span>(<span class="hljs-params">text</span>):</span>
  in_fpath = Path(<span class="hljs-string">"donald_trump_hosts_medal_presentation_ceremony_-820681363564909524.wav"</span>) <span class="hljs-comment"># 特朗普的一小段声音文件</span>
  reprocessed_wav = encoder.preprocess_wav(in_fpath)
  original_wav, sampling_rate = librosa.load(in_fpath)
  preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
  embed = encoder.embed_utterance(preprocessed_wav)
  <span class="hljs-built_in">print</span>(<span class="hljs-string">"Synthesizing new audio..."</span>)
  <span class="hljs-keyword">with</span> io.capture_output() <span class="hljs-keyword">as</span> captured:
    specs = synthesizer.synthesize_spectrograms([text], [embed])
  generated_wav = vocoder.infer_waveform(specs[<span class="hljs-number">0</span>])
  generated_wav = np.pad(generated_wav, (<span class="hljs-number">0</span>, synthesizer.sample_rate), mode=<span class="hljs-string">"constant"</span>)
  librosa.output.write_wav(<span class="hljs-string">"output_trump_voice.wav"</span>, generated_wav, synthesizer.sample_rate) 
  display(Audio(generated_wav, rate=synthesizer.sample_rate))
  
synth(<span class="hljs-string">"Chinese government is so powerful, and I love the Republic of China"</span>) <span class="hljs-comment"># 合成语音</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后的生成效果如下：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fnladuo.github.io%2Ftrump_voice_generated.wav" target="_blank" rel="nofollow noopener noreferrer" title="http://nladuo.github.io/trump_voice_generated.wav" ref="nofollow noopener noreferrer">nladuo.github.io/trump_voice…</a></p>
<p>完整的代码：链接:<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpan.baidu.com%2Fs%2F1NFtU26GW1O0koF-pHrxALA" target="_blank" rel="nofollow noopener noreferrer" title="https://pan.baidu.com/s/1NFtU26GW1O0koF-pHrxALA" ref="nofollow noopener noreferrer">pan.baidu.com/s/1NFtU26GW…</a>  密码:ezl8</p>
<p>本文代码可查看<code>demo_trump_voice_sythesis.ipynb</code>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27d479f1539d4fb28d8eceee5fcbb63c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            