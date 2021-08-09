
---
title: 'React旺财记账-标签页基础功能制作'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2479'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 01:58:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=2479'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">抽离useTags函数</h1>
<pre><code class="copyable">import &#123;useState&#125; from "react";

const useTags = () => &#123;//自定义hook必须use开头
    const [tags, setTags] = useState<string[]>(['衣', '食', '住', '行']);
    return &#123;tags, setTags&#125;//后期可以研究为什么必须导出对象而不是数组
    //缩写tags:tags,setTags:setTags
&#125;

export &#123;useTags&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：自定义hook必须use开头</p>
</blockquote>
<h1 data-id="heading-1">tagList样式</h1>
<pre><code class="copyable">import Layout from "../components/Layout";
import React from "react";
import &#123;useTags&#125; from "../useTags";
import styled from "styled-components";
import Icon from "components/Icon";

const Taglist = styled.ol`
  font-size: 16px;
  background: white;

  > li &#123;
    border-bottom: 1px solid #d5d5d9;
    line-height: 20px;
    padding: 12px 16px 12px 0;
    margin-left: 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  &#125;
`

const Button = styled.button`
  font-size: 18px;
  border: none;
  padding: 8px 12px;
  background: #ffd833;
  border-radius: 4px;
`

const Center=styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
`

const Space=styled.div`
    height: 16px;
`

function Tags() &#123;
    const &#123;tags, setTags&#125; = useTags();//析构
    return (
        <Layout>
            <Taglist>
                &#123;tags.map(tag =>
                    <li key=&#123;tag&#125;>
                        <span className="oneLine">&#123;tag&#125;</span>
                        <Icon name="right"/>
                    </li>)&#125;
            </Taglist>
            <Center>
                <Space/>
                <Space/>
                <Space/>
                <Button>新增标签</Button>
                <Space/>
            </Center>
        </Layout>
    )
&#125;

export default Tags;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">改变tag的类型</h1>
<ul>
<li>在之前的程序中，我们的tag类型为string，存放标签名。但是当用户想要更改标签名时，该标签所对应的数据也得做出改变，这很不方便。</li>
<li>将tag改为带有id和name的类型就可以避免这种情况。因为id是不变的。</li>
</ul>
<pre><code class="copyable">import &#123;useState&#125; from "react";

const useTags = () => &#123;//自定义hook必须use开头
    const [tags, setTags] = useState<&#123; id: number; name: string &#125;[]>([
        &#123;id: 1, name: '衣'&#125;,
        &#123;id: 2, name: '食'&#125;,
        &#123;id: 3, name: '住'&#125;,
        &#123;id: 4, name: '行'&#125;
    ]);
    return &#123;tags, setTags&#125;//后期可以研究为什么必须导出对象而不是数组
&#125;

export &#123;useTags&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：修改类型后，其他对应代码也需要修改</p>
<p>小技巧：</p>
<ol>
<li>WebStorm改名需要选中右键在菜单中单击rename，这样可以改整个文档</li>
<li>改变某数据类型时，想找到它的类型定义。可以在该数据定义行，按住ctrl+单击内容，即可自动跳转</li>
</ol>
</blockquote>
<h1 data-id="heading-3">createId函数</h1>
<pre><code class="copyable">//函数写法
let id = 0
const createId = () => &#123;
    id += 1;
    return id;
&#125;

export &#123;createId&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在所有具有id生成的地方，都用 <code>createId()</code> 这个函数来生成</p>
<pre><code class="copyable">import &#123;useState&#125; from "react";
import &#123;createId&#125; from "./lib/createId";

const defaultTags=[//防止每次调用，id都会重新生成
    &#123;id: createId(), name: '衣'&#125;,
    &#123;id: createId(), name: '食'&#125;,
    &#123;id: createId(), name: '住'&#125;,
    &#123;id: createId(), name: '行'&#125;
]

const useTags = () => &#123;//自定义hook必须use开头
    const [tags, setTags] = useState<&#123; id: number; name: string &#125;[]>(defaultTags);
    return &#123;tags, setTags&#125;//后期可以研究为什么必须导出对象而不是数组
&#125;

export &#123;useTags&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//类写法
let id = 0

class Id &#123;
    value: number;
    constructor() &#123;
        id += 1;
        this.value = id
    &#125;
&#125;

export &#123;Id&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>用法：<code>new Id</code></li>
<li>好处：封装操作可以更多</li>
</ul>
<h1 data-id="heading-4">useParams与findTag</h1>
<p>封装findTag到useTags</p>
<pre><code class="copyable">const findTag = (id: number) => tags.filter(tag => tag.id === id)[0];
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import React from "react";
import &#123;useTags&#125; from "../useTags";
import &#123;useParams&#125; from "react-router-dom";

type Params=&#123;
    id:string
&#125;
const TagEdit: React.FunctionComponent = () => &#123;
    const &#123;findTag&#125; = useTags()
    let &#123;id&#125; = useParams<Params>();
    const tag = findTag(parseInt(id))
    return (
        <div>&#123;tag.name&#125;</div>
    )
&#125;

export &#123;TagEdit&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            