
---
title: '學習Solidity之Hello world'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/e7fa8670-bee7-4695-a48f-f11db338b90b.png'
author: Matters
comments: false
date: Sun, 24 Apr 2022 15:20:42 GMT
thumbnail: 'https://assets.matters.news/embed/e7fa8670-bee7-4695-a48f-f11db338b90b.png'
---

<div>   
<p>開發工具與環境設置</p><p>安裝所需要工具</p><pre class="ql-syntax" spellcheck="false">npm install -g truffle ganache-cli
</pre><p>啟動 ganache-cli來啟動乙太坊測試環境</p><pre class="ql-syntax" spellcheck="false">ganache-cli
</pre><figure class="image"><img src="https://assets.matters.news/embed/e7fa8670-bee7-4695-a48f-f11db338b90b.png" data-asset-id="e7fa8670-bee7-4695-a48f-f11db338b90b" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><figure class="image"><img src="https://assets.matters.news/embed/068be6ee-dfb4-476c-b6c3-43933df9ff87.png" data-asset-id="068be6ee-dfb4-476c-b6c3-43933df9ff87" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p><br></p><p>建立智能合約</p><pre class="ql-syntax" spellcheck="false">mkdir hello
cd hello
truffle init
truffle create contract HelloWorld #建立合約
</pre><figure class="image"><img src="https://assets.matters.news/embed/fbddc99f-f761-4638-ac31-032a295d8a67.png" data-asset-id="fbddc99f-f761-4638-ac31-032a295d8a67" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><figure class="image"><img src="https://assets.matters.news/embed/a54c69ce-221e-4827-8504-24a935367237.png" data-asset-id="a54c69ce-221e-4827-8504-24a935367237" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p><br></p><p>HelloWorld.sol:</p><pre class="ql-syntax" spellcheck="false">// SPDX-License-Identifier: MIT pragma solidity >=0.4.22 <0.9.0; contract HelloWorld &#123;  // constructor() public &#123;  // &#125;  function sayHello() public pure returns (string memory)&#123;    return ("Hello World");  &#125; &#125;
</pre><p>編譯</p><pre class="ql-syntax" spellcheck="false">truffle compile
</pre><p>編譯成功的話，在build/contracts/目錄下會多出HelloWorld.json這個檔案</p><figure class="image"><img src="https://assets.matters.news/embed/33f5c438-9668-4859-b787-6e62b4ba5d17.png" data-asset-id="33f5c438-9668-4859-b787-6e62b4ba5d17" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>部署</p><p>在migrate中新增2\_deploy\_contracts.js</p><p>(migration檔案會依照檔案的編號來執行。例如2\_就會在1\_之後執行。檔案後面的文字只為協助開發者理解之用)</p><figure class="image"><img src="https://assets.matters.news/embed/6e9bffaa-0b2c-41bc-9b95-4ad43d1e10d9.png" data-asset-id="6e9bffaa-0b2c-41bc-9b95-4ad43d1e10d9" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>2\_deploy\_contracts.js:</p><pre class="ql-syntax" spellcheck="false">var HelloWorld = artifacts.require("HelloWorld");

module.exports = function(deployer) &#123;
 deployer.deploy(HelloWorld);
&#125;;
</pre><p>區塊網路設定</p><p>在truffle-config檔案裡L</p><figure class="image"><img src="https://assets.matters.news/embed/8ae6faa0-76e9-4dca-91ef-8a667912b3a7.png" data-asset-id="8ae6faa0-76e9-4dca-91ef-8a667912b3a7" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>加入設定</p><figure class="image"><img src="https://assets.matters.news/embed/308b5bd4-62a7-45f7-bfa6-2bb8d6fbd6d2.png" data-asset-id="308b5bd4-62a7-45f7-bfa6-2bb8d6fbd6d2" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>開始部署:</p><pre class="ql-syntax" spellcheck="false">truffle migrate
</pre><figure class="image"><img src="https://assets.matters.news/embed/09336303-0cea-406c-b71a-06d64c7e0181.png" data-asset-id="09336303-0cea-406c-b71a-06d64c7e0181" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>測試</p><p>使用truffle提供的命令行工具，執行:</p><pre class="ql-syntax" spellcheck="false">truffle console
</pre><p>輸入</p><pre class="ql-syntax" spellcheck="false">> let contract
> HelloWorld.deployed().then(instance => contract = instance)
> contract.sayHello.call()
</pre><figure class="image"><img src="https://assets.matters.news/embed/f848a5cf-0bfa-4c6b-b28e-38f48e0dcc35.png" data-asset-id="f848a5cf-0bfa-4c6b-b28e-38f48e0dcc35" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><figure class="image"><img src="https://assets.matters.news/embed/70194fee-7f67-4ce0-9ae8-dbe165a6a09c.png" data-asset-id="70194fee-7f67-4ce0-9ae8-dbe165a6a09c" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p><strong>## 我的名子合約</strong></p><p>> 輸入名子，並藉由呼叫函數來顯示</p><p>MyName.sol:</p><pre class="ql-syntax" spellcheck="false">// SPDX-License-Identifier: MIT pragma solidity >=0.4.22 <0.9.0; contract MyName &#123; string public _name; constructor() &#123; _name="Please Type Your Name"; &#125; function setName(string memory name) public&#123; _name = name ; &#125; function getName() public view returns (string memory)&#123; return _name; &#125; &#125;
</pre><p>編譯並佈署後</p><p>我們開始測試</p><pre class="ql-syntax" spellcheck="false">truffle console
let contract
MyName.deployed().then(instance => contract = instance)
</pre><p><br></p><figure class="image"><img src="https://assets.matters.news/embed/a3dca34f-8d60-4cd3-a6db-9eb455a3332c.png" data-asset-id="a3dca34f-8d60-4cd3-a6db-9eb455a3332c" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><p>call function:</p><pre class="ql-syntax" spellcheck="false">contract.getName.call()
contract.setName("Test Name")
</pre><figure class="image"><img src="https://assets.matters.news/embed/163076d8-81d5-47a4-889a-18c1a71120d5.png" data-asset-id="163076d8-81d5-47a4-889a-18c1a71120d5" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><pre class="ql-syntax" spellcheck="false">contract.getName.call()
</pre><figure class="image"><img src="https://assets.matters.news/embed/a9ac558d-92bb-437c-9856-08ad526e24c3.png" data-asset-id="a9ac558d-92bb-437c-9856-08ad526e24c3" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p><br></p><hr><p><br></p><p>歡迎大家來我的<a href="https://www.fufunote.com/" rel="noopener noreferrer" target="_blank">Blog</a>看:</p><p>1.Blog: <a href="https://www.fufunote.com/2021/ad49/" rel="noopener noreferrer" target="_blank">文章連結</a></p><p><br></p><p><br></p>  
</div>
            