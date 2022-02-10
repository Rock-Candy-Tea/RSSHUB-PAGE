
---
title: 'Vim 的中文支持及解决思路'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://picsum.photos/400/300?random=586'
author: 少数派 sspai
comments: false
date: Tue, 08 Feb 2022 09:57:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=586'
---

<div>   
<div class="articleWidth-content" data-v-0b37afcb><div class="update-wrap" data-v-0b37afcb></div><div class="content wangEditor-txt minHeight" data-v-0b37afcb><p>用 Vim 编辑中文时，有两个独有的小问题：输入法切换；中文文章中光标跳转。</p><h2>输入法切换</h2><p>在插入模式和普通模式之间切换时，应该分别对应中文输入法和英文输入法（或中文输入法的英文状态）。</p><p>Vim 需要在两种模式之间频繁切换，每次都要切换输入法状态会产生干扰，打断心流。</p><p>解决方案有两个思路：输入法级的方案，和 Vim 级的方案。</p><h3>1. 输入法级的方案</h3><p>一些输入法提供了在特定软件中使用特定输入法的设置，例如搜狗拼音。但是它似乎没办法识别当前是在 Vim 的哪一种模式下。</p><p>开源输入法引擎中州韵（在 Mac 上叫"鼠须管", 在 Windows 上叫"小狼毫") 提供了更细的控制：它有个叫 <a href="https://einverne.github.io/post/2020/11/rime-auto-switch-language-in-vim-mode.html">vim_mode</a> 的开关，可以根据 Vim 的所在模式自动切换。在 squirrel.custom.yaml 中配置即可。</p><pre class="language-shell"><code>app_options:
    org.vim.MacVim:
        ascii_punct: true
        vim_mode: true
    vim:
        ascii_punct: true
        vim_mode: true</code></pre><p>在这个配置里，除了打开 vim_mode 的开关外，还设置了在 Vim 或 MacVim 中使用英文标点。这在写代码时很好用，能避免用错标点导致的错误。在写中文文章时，可以用 <a href="https://github.com/hotoo/pangu.vim">Pangu</a> 之类的插件自动处理一下就好了。</p><h3>2. Vim 级的方案</h3><p>也可以完全不考虑输入法，让插件来改变输入法状态。有一个叫 <a href="https://github.com/ybian/smartim">smart-im</a> 的插件，可以很好地实现这一功能。</p><h2>中文文章跳转</h2><p>写英文或代码时，w 和 W 是常用的跳转方式。但是中文不用空格来分词，所以 w 会以逗号和句号为分隔符来跳转；如果使用的是中文标点，情况就更糟。</p><p>这个问题难以解决；它是个自然语言处理问题，得让计算机稍微懂一点中文才行。</p><p>要稍微迂回地解决这个问题，大概有三种思路。</p><h3>1. 使用插件</h3><p>Vim 的中文分词插件不多，可能因为这是个有点奇怪的需求。</p><p>在 Github 上有个叫 <a href="https://github.com/fannheyward/coc-ci">coc-ci</a> 的中文分词插件，以 <a href="https://github.com/neoclide/coc.nvim">coc.nvim</a> 为基础（顺便，coc.nvim 很强，建议安装）。但是 coc-ci 的速度太慢，按一下 w 要一秒多钟才会跳到下一个词。这显然是不可接受的。</p><p>也许是我的机器有什么配置问题吧。但是实在不想折腾，所以换了种思路：预处理。</p><h3>2. 对中文文稿预处理</h3><p>预处理的思路是：找中文分词工具把中文文稿处理一遍，编辑完后再去掉分隔符。</p><p>对比开源中文分词工具的过程略过，最后选择了 <a href="https://github.com/thunlp/THULAC-Python">thulac</a> 。只要三行 python 代码，就能让它预处理一下要编辑的文稿，在词之间加上空格。</p><p>接下来正常编辑，完成后只需要再全局查找替换一下空格就可以了。</p><p>这个方案的问题是，查找替换空格往往会误删掉有用的空格，例如 Markdown 标签后的空格、链接两侧的空格、英文单词间的空格等等。虽然可以写一些规则来避免，但是逐一添加白名单的方式有点笨。</p><p>所以换一种思路：如果放弃中文分词的尝试呢？</p><h3>3. 关键是快速移动</h3><p>不要搞错了重点。我们的目的不是中文分词，而是在中文文稿中快速移动。</p><p>快速移动无非两种思路：机枪乱扫和精准点射。</p><p>使用 w 命令的移动是前者，按住键不放就可以了，视线会自动跟随光标移动。修改一下 Mac 默认的击键重复速度，速度还是挺快的。它的好处在于减少认知负担，就算跑过了头，再按 b 往回跳就行了。</p><p>即使是在 Mac 的系统设置面板中将击键重复速度调到最快，对使用 Vim 来说还是有些慢。可以在终端直接设置来让它变得更快：</p><pre class="language-shell"><code># normal minimum is 15 (225 ms)
defaults write -g InitialKeyRepeat -int 10
# normal minimum is 2 (30 ms)
defaults write -g KeyRepeat -int 1</code></pre><p>当然，这样的调整对英文和代码很有用，但对于中文用处不大。</p><p>精准点射的思路是，先看好要跳去哪里，然后再用命令组合跳转。这不免会涉及到计算，是难以自动化的。</p><p>不过有一个插件，能够减少计算的难度：<a href="https://github.com/easymotion/vim-easymotion">vim-easymotion</a> 插件。它和 Chrome 上的 <a href="https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb?utm_source=chrome-ntp-icon">Vimium</a> 有些相似。使用快捷键激活后，可以输入对应内容直接跳到相应位置。无论是以词为单位，还是在当前行或者当前列，都很方便。</p><p>我的 vimrc 是这样配置的：</p><pre class="language-shell"><code>" 查找一个字符
map  <Leader>i <Plug>(easymotion-bd-f)
nmap <Leader>i <Plug>(easymotion-overwin-f)

" 查找任意长度字符串
" 好像比默认的"/"还方便
nmap <leader>s <Plug>(easymotion-sn)

" 跳到任意行
omap <C-L> <Plug>(easymotion-bd-jk)
nmap <C-L> <Plug>(easymotion-overwin-line)

" 跳到任意单词
omap <Leader>w <Plug>(easymotion-bd-w)
nmap <Leader>w <Plug>(easymotion-overwin-w)

" 单方向标记可以跳转的位置
map <Leader>l <Plug>(easymotion-lineforward)
map <Leader>j <Plug>(easymotion-j)
map <Leader>k <Plug>(easymotion-k)
map <Leader>h <Plug>(easymotion-linebackward)

" 以当前光标所在列为标记基准
let g:EasyMotion_startofline = 0

" 更聪明的大小写判断
" 小写字母会匹配小写和大写
" 大写字母只匹配大写
let g:EasyMotion_smartcase = 1
</code></pre><p> </p><p>这样，算是基本解决了 Vim 中文编辑的问题。</p></div><div class="update-details-wrap" data-v-0b37afcb></div><!----></div><div style="border:1px solid transparent;" data-v-0b37afcb></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-0b37afcb><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>4</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>2</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-3730" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90Vim%20%E7%9A%84%E4%B8%AD%E6%96%87%E6%94%AF%E6%8C%81%E5%8F%8A%E8%A7%A3%E5%86%B3%E6%80%9D%E8%B7%AF%E3%80%91%E7%94%A8Vim%E7%BC%96%E8%BE%91%E4%B8%AD%E6%96%87%E6%97%B6%EF%BC%8C%E6%9C%89%E4%B8%A4%E4%B8%AA%E7%8B%AC%E6%9C%89%E7%9A%84%E5%B0%8F%E9%97%AE%E9%A2%98%EF%BC%9A%E8%BE%93%E5%85%A5%E6%B3%95%E5%88%87%E6%8D%A2%EF%BC%9B%E4%B8%AD%E6%96%87%E6%96%87%E7%AB%A0%E4%B8%AD%E5%85%89%E6%A0%87%E8%B7%B3%E8%BD%AC%E3%80%82%E8%BE%93%E5%85%A5%E6%B3%95%E5%88%87%E6%8D%A2%E5%9C%A8%E6%8F%92%E5%85%A5%E6%A8%A1%E5%BC%8F%E5%92%8C%E6%99%AE%E9%80%9A%E6%A8%A1%E5%BC%8F%E4%B9%8B%E9%97%B4%E5%88%87%E6%8D%A2%E6%97%B6%EF%BC%8C%E5%BA%94%E8%AF%A5%E5%88%86%E5%88%AB%E5%AF%B9%E5%BA%94%E4%B8%AD%E6%96%87%E8%BE%93%E5%85%A5%E6%B3%95%E5%92%8C%E8%8B%B1%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-8639" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90Vim%20%E7%9A%84%E4%B8%AD%E6%96%87%E6%94%AF%E6%8C%81%E5%8F%8A%E8%A7%A3%E5%86%B3%E6%80%9D%E8%B7%AF%E3%80%91%E7%94%A8Vim%E7%BC%96%E8%BE%91%E4%B8%AD%E6%96%87%E6%97%B6%EF%BC%8C%E6%9C%89%E4%B8%A4%E4%B8%AA%E7%8B%AC%E6%9C%89%E7%9A%84%E5%B0%8F%E9%97%AE%E9%A2%98%EF%BC%9A%E8%BE%93%E5%85%A5%E6%B3%95%E5%88%87%E6%8D%A2%EF%BC%9B%E4%B8%AD%E6%96%87%E6%96%87%E7%AB%A0%E4%B8%AD%E5%85%89%E6%A0%87%E8%B7%B3%E8%BD%AC%E3%80%82%E8%BE%93%E5%85%A5%E6%B3%95%E5%88%87%E6%8D%A2%E5%9C%A8%E6%8F%92%E5%85%A5%E6%A8%A1%E5%BC%8F%E5%92%8C%E6%99%AE%E9%80%9A%E6%A8%A1%E5%BC%8F%E4%B9%8B%E9%97%B4%E5%88%87%E6%8D%A2%E6%97%B6%EF%BC%8C%E5%BA%94%E8%AF%A5%E5%88%86%E5%88%AB%E5%AF%B9%E5%BA%94%E4%B8%AD%E6%96%87%E8%BE%93%E5%85%A5%E6%B3%95%E5%92%8C%E8%8B%B1%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            