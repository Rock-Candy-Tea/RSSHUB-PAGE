
---
title: '聊聊go-ddd-sample'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=6209'
author: 掘金
comments: false
date: Mon, 22 Mar 2021 08:00:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=6209'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">序</h2>
<p>本文主要赏析一下go-ddd-sample</p>
<h2 data-id="heading-1">项目结构</h2>
<pre><code class="copyable">├── _sql
├── application
├── config
├── domain
│   └── repository
├── infrastructure
│   └── persistence
│       └── testdata
└── interfaces
    └── testdata
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里分为application、domain、infrastructure、interfaces四层</p>
</blockquote>
<h2 data-id="heading-2">domain</h2>
<pre><code class="copyable">├── repository
│   ├── mock_user.go
│   └── user.go
└── user.go
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>domain层定义了模型及repository接口，同时利用go generate生成repository的mock实现</p>
</blockquote>
<h2 data-id="heading-3">application</h2>
<pre><code class="copyable">// UserInteractor provides use-case
type UserInteractor struct &#123;
Repository repository.UserRepository
&#125;

// GetUser returns user
func (i UserInteractor) GetUser(ctx context.Context, id int) (*domain.User, error) &#123;
return i.Repository.Get(ctx, id)
&#125;

// GetUsers returns user list
func (i UserInteractor) GetUsers(ctx context.Context) ([]*domain.User, error) &#123;
return i.Repository.GetAll(ctx)
&#125;

// AddUser saves new user
func (i UserInteractor) AddUser(ctx context.Context, name string) error &#123;
u, err := domain.NewUser(name)
if err != nil &#123;
return err
&#125;
return i.Repository.Save(ctx, u)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>applicatioin层调用domain层来进行业务编排</p>
</blockquote>
<h2 data-id="heading-4">infrastructure</h2>
<pre><code class="copyable">└── persistence
    ├── main_test.go
    ├── testdata
    │   ├── schema.sql -> ../../../_sql/schema.sql
    │   └── users.yml
    ├── user_repository.go
    └── user_repository_test.go
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>infrastructure的persistence实现了domain层定义的repository接口</p>
</blockquote>
<h2 data-id="heading-5">interfaces</h2>
<pre><code class="copyable">├── handler.go
├── handler_test.go
├── main_test.go
└── testdata
    ├── schema.sql -> ../../_sql/schema.sql
    └── users.yml
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>interfaces基于net/http来提供http接口</p>
</blockquote>
<h2 data-id="heading-6">小结</h2>
<p>go-ddd-sample分为application、domain、infrastructure、interfaces四层，其中domain定义repository接口，infrastructure层实现该接口，application层通过domain来编排业务逻辑，interfaces层则基于net/http来提供http接口。</p>
<h2 data-id="heading-7">doc</h2>
<ul>
<li><a href="https://github.com/takashabe/go-ddd-sample" target="_blank" rel="nofollow noopener noreferrer">go-ddd-sample</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            