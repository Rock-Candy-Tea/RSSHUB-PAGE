
---
title: 'A Deep Dive Into Logbook Smart Contract'
categories: 
 - 新媒体
 - Matters
 - 最新、熱議、精華
headimg: 'https://assets.matters.news/embed/03bf3151-d46c-4c16-860b-2373fd15d21d.png'
author: Matters
comments: false
date: Fri, 25 Mar 2022 09:58:09 GMT
thumbnail: 'https://assets.matters.news/embed/03bf3151-d46c-4c16-860b-2373fd15d21d.png'
---

<div>   
<p>On experimenting with digital ownership, <a href="https://matters-lab.io/" rel="noopener noreferrer" target="_blank">Matters Lab</a> is blurring the line between private and public ownership with three Web3 projects: <a href="https://traveloggers.matters.news/" rel="noopener noreferrer" target="_blank">Traveloggers</a>, a profile picture (pfp) NFT on private ownership; <a href="https://twitter.com/thespace2022" rel="noopener noreferrer" target="_blank">The Space</a>, a draw-to-earn pixel canvas with Universal Basic Income (UBI) and Harberger Tax on common ownership; And, <a href="https://logbook.matters.news/" rel="noopener noreferrer" target="_blank">Logbook</a>, a co-creation writing dApp on collective ownership.</p><p>Logbook originated as a feature of Traveloggers, allowing NFT owners to write down thoughts on Ethereum blockchain. As the pain of gas fees and new ideas on collaborative content arise, we redesigned the Logbook smart contract with many new features: lower gas fee, fork and donation, royalty-splitting, decentralized frontend, and on-chain NFT. </p><p>You don't completely own your NFTs. Each logbook is an NFT, you have rights to transfer and benefit from your writing. But it's open to fork, like open-source software, once public, never stop. Anyone can use or fork your code, live and rebirth in other projects, your code commits remain. Logbook is the same, your content is still yours, but it can be in any logbook.</p><h2>Overview</h2><p>We have three GitHub repositories about Logbook:</p><ul><li><a href="https://github.com/thematters/logbook" rel="noopener noreferrer" target="_blank">thematters/logbook</a>: Logbook web app, hosting on <a href="https://logbook.matters.news/" rel="noopener noreferrer" target="_blank">logbook.matters.news</a>;</li><li><a href="https://github.com/thematters/subgraphs" rel="noopener noreferrer" target="_blank">thematters/subgraph</a>: The Graph subgraph;</li><li><a href="https://github.com/thematters/contracts" rel="noopener noreferrer" target="_blank">thematters/contracts</a>: Logbook smart contract, deployed on <a href="https://polygonscan.com/address/0xcdf8d568ec808de5fcbb35849b5bafb5d444d4c0" rel="noopener noreferrer" target="_blank">PolygonScan</a>;</li></ul><p>Writing a secure, gas-efficient, and easy-to-read smart contract is hard, especially in this fast-growing and highly uncertain industry. We would love to share more details on how we design and implement the Logbook smart contract. </p><p><a href="https://hardhat.org/" rel="noopener noreferrer" target="_blank">Hardhat</a>, the most popular Solidity development environment, provides a smooth experience for JavaScript developers and excellent extensibility through plugins, but context switching hurts productivity. We write contracts in Solidity but tests in JavaScript. Even worse, we have to deal with the large package dependencies. Thanks to <a href="https://github.com/gakonst/foundry/" rel="noopener noreferrer" target="_blank">Foundry</a>, we can build faster, test better, all in Solidity.</p><p>Diving into the <code>src/Logbook/Logbook.sol</code>, we can see the dependencies of the Logbook contract:</p><pre class="ql-syntax" spellcheck="false">Logbook
 ↖ ERC721
 ↖ Ownable
 ↖ Royalty
</pre><p><code>ERC721</code> is the implementation of <a href="https://eips.ethereum.org/EIPS/eip-721" rel="noopener noreferrer" target="_blank">ERC-721 standard</a> from OpenZeppelin, <code>Ownable</code> allows an address to call claim logbook function and change public sale status (Traveloggers can claim logbook for free, after that, they can be minted from public sale).</p><p>At the core, <code>Logbook</code> inherits from <code>Royalty</code>, contains business logic on how a logbook can be minted, how the owner can interact with the logbook, and how to split royalty from fork and donation.</p><p>For blockchain platform, we chose Polygon, mainly because of the low gas fee and the mature ecosystem. As developers, we can use services like Alchemy and The Graph. As creators, we can buy/sell Logbook NFT on OpenSea, swap the incomes to stablecoins on Uniswap, etc.</p><p>Last but not least, to query contract data more accessible, we use <a href="https://thegraph.com/" rel="noopener noreferrer" target="_blank">The Graph</a>, a decentralized indexing service that provides <a href="https://thegraph.com/hosted-service/subgraph/thematters/logbook" rel="noopener noreferrer" target="_blank">GraphQL API</a> for clients.</p><h2>Royalty-Splitting and Decentralized Frontend</h2><p><br></p><figure class="image"><img src="https://assets.matters.news/embed/03bf3151-d46c-4c16-860b-2373fd15d21d.png" data-asset-id="03bf3151-d46c-4c16-860b-2373fd15d21d" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>Let’s take a closer look at external functions:</p><pre class="ql-syntax" spellcheck="false">// src/Logbook/ILogbook.sol
ILogbook
  - setTitle
  - setDescription
  - publish
  - getLogbook
  - getLogs
  - setForkPrice
  - fork
  - forkWithCommission
  - donate
  - donateWithCommission
  - ...

// src/Logbook/IRoyalty.sol
IRoyalty
  - withdraw
  - getBalance
</pre><p><code>setTitle</code>, <code>setDescription</code> and <code>publish</code> are for owners to update the logbook. <code>getLogbook</code> and <code>getLogs</code> just simple getters to get details of a logbook. With these interfaces, we can already make a nice dApp that creators can publish content on-chain. But there is more than that. Creators can make money from their work.</p><p>Anyone can donate $MATIC to a logbook, or the owner can set a fork price (<code>setForkPrice</code>) allowing others to fork the logbook and continue to write. 80% of these incomes goes to the owner, the rest, up to 20%, are equally divided to contents' authors. If some contents are inherited from the fork, the original authors get this share.</p><p>Why up to 20%? It depends on how users call the functions. </p><p>Most of the time, users view content or interact with contracts via a website. Although Matters Lab designed and built <a href="https://logbook.matters.news/" rel="noopener noreferrer" target="_blank">logbook.matters.news</a>, it's centralized, our taste, our limitation. By leveraging these contract interfaces, developers can make a customized frontend by themselves, for others, and take a commission from <code>forkWithCommission</code> and <code>donateWithCommission</code>. Assume a developer created a Logbook web app with great UI/UX, readers and creators love to use it. Since maintaining and hosting it costs time and money, the developer decides to take a 5% cut from every fork and donation. Win-Win!</p><p>Function parameters <code>commission_</code> (the address to receive the commission) and <code>commissionBPS_</code> (the percentage of the commission in basis points) can be passed into <code>forkWithCommission</code> and <code>donateWithCommission</code>. The <code>commissionBPS_</code> is capped at 2,000 (20%), which means the developer can decide how much an address takes after the logbook owner takes 80% of the fees.</p><p>Join to hack the Logbook!</p><h2>Gas Optimization</h2><figure class="image"><img src="https://assets.matters.news/embed/9153f9ef-8570-4cb4-99d7-37ec649bd5fd.png" data-asset-id="9153f9ef-8570-4cb4-99d7-37ec649bd5fd" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>Blockchain, as its name, is a chain consisting of data blocks. A block contains a limited number of transactions. Transaction fee goes to miners of the blockchain network who confirm the service requests, by providing computation and storage resources. Although Moore's Law makes these resources abundant, decentralized service is scarce. We are paying for the promise of decentralization, bidding with a gas price.</p><p>So what efforts have we made to fight this scarcity of abundance?</p><p><strong>Space. </strong></p><p>Different EVM opcode executed in a transaction costs different units of gas. One of the most expensive opcodes is <code><a href="https://www.evm.codes/#55" rel="noopener noreferrer" target="_blank">SSTORE</a></code>, to put data into the contract storage, maximum ~20,000 gas per storage slot (32-byte). We should store minimal data on storage.</p><p>There are several gas-efficient ways to store data: stateless contract, off-chain storage, and emitting data as an event. For stateless contracts, data is passed to functions that do nothing. For off-chain storage, data is stored on storage services like IPFS or Arweave, then submit the identifier (URL, CID, etc.) on-chain. Both solutions aren't easy to access the data by the client. We took the last one, data are emitted as events using <code><a href="https://www.evm.codes/#a1" rel="noopener noreferrer" target="_blank">LOG*</a></code> opcodes, saving ~90% gas compares to <code>SSTORE</code>, besides, clients can retrieve on-chain data with topic filters directly or using The Graph API.</p><p>Another optimization is on the data structure. Logbook supports collaborative content creation, a logbook can be forked by anyone without the owner's permission, with inherited contents.</p><p>Instead of copying data from the parent, we can just link to it with a minimal set of metadata.</p><pre class="ql-syntax" spellcheck="false">// https://github.com/thematters/contracts/blob/81246e4/src/Logbook/ILogbook.sol#L26-L41

struct Book &#123;
    // end position of a range of logs
    uint32 endAt;
    // parent book
    uint256 parent;
    // all logs hashes in the book
    bytes32[] contentHashes;
    ...
&#125;
</pre><p>Finally, the gas of content publishing is dropped up to 90%. With Polygon, the cost in USD dropped up to 99.99%!</p><figure class="image"><img src="https://assets.matters.news/embed/9883b543-fff2-4b06-8aa7-89ceaa40faca.png" data-asset-id="9883b543-fff2-4b06-8aa7-89ceaa40faca" referrerpolicy="no-referrer"><figcaption><span>Gas Price = 30 Gwei, 1 MATIC ≈ 1.5 USD, 1 ETH ≈ 3000 USD</span></figcaption></figure><p><strong>Time.</strong></p><p>Block has a gas limit, of <a href="https://polygonscan.com/blocks" rel="noopener noreferrer" target="_blank">30M</a> on Polygon, so a transaction may run out of gas. Royalty-splitting iterates contents and updates the author's balance. <code>SSTORE</code> costs ~20,000 gas if the slot is a zero value, but only ~5,000 if it's non-zero, a vast difference!</p><pre class="ql-syntax" spellcheck="false">// https://github.com/thematters/contracts/blob/81246e4/src/Logbook/Logbook.sol#L387-L397

for (uint32 i = 0; i < logCount; i++) &#123;
  Log memory log = logs[contentHashes[i]];
  _balances[log.author] += fees.perLogAuthor;
  ...
&#125;
</pre><p>We did a little trick to maximize the number of iterations that can be run. The balance of an address will always be a non-zero value once it owns a token. In the long run, the bottleneck on gas limit is mitigated by distributing to specific transactions in different blocks. </p><pre class="ql-syntax" spellcheck="false">// https://github.com/thematters/contracts/blob/81246e4/src/Logbook/Logbook.sol#L401-L414

function _afterTokenTransfer(
  address from_,
  address to_,
  uint256 tokenId_
) internal virtual override &#123;
  ...
  if (_balances[to_] == 0) &#123;
    _balances[to_] = 1 wei;
  &#125;
&#125;

// https://github.com/thematters/contracts/blob/81246e4/src/Logbook/Royalty.sol#L12-L24

function withdraw() public &#123;
  ...
  _balances[msg.sender] = 1 wei;
  ...
&#125;
</pre><h2>On-chain NFT</h2><figure class="image"><img src="https://assets.matters.news/embed/69094df5-8447-443f-a4b6-3ecc760cfeb6.gif" data-asset-id="69094df5-8447-443f-a4b6-3ecc760cfeb6" referrerpolicy="no-referrer"><figcaption><span></span></figcaption></figure><p>Logbook is not only an on-chain writing dApp but also a <a href="https://opensea.io/collection/traveloggers-logbook" rel="noopener noreferrer" target="_blank">generative NFT collection</a>. Every publishing or transfer will change the colors of the image. Under the <a href="https://eips.ethereum.org/EIPS/eip-170" rel="noopener noreferrer" target="_blank">24KB</a> contract code size limit, SVG is light and flexible, an ideal format to generate images on-chain.</p><p>Another limit is when concatenating a large string. It's pretty easy to see the <a href="https://soliditydeveloper.com/stacktoodeep" rel="noopener noreferrer" target="_blank">"Stack Too Deep"</a> error. To solve it, we can pack the parameters with <code>struct</code> and split <code>generateSVG</code> into four functions:</p><pre class="ql-syntax" spellcheck="false">// https://github.com/thematters/contracts/blob/81246e487008740f3515b7a6c91c7c43b58262dd/src/Logbook/NFTSVG.sol

struct SVGParams &#123;
  uint32 logCount;
  uint32 transferCount;
  uint160 createdAt;
  uint256 tokenId;
&#125;

function generateSVG(SVGParams memory params) internal pure returns (string memory svg) &#123;
  svg = string(
    abi.encodePacked(
            '<svg width="800" height="800" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd">',
      generateSVGBackground(params),
      generateSVGPathsA(params),
      generateSVGPathsB(params),
      generateSVGTexts(params),
      "</g></svg>"
    )
  );
&#125;

function generateSVGBackground() &#123;&#125;
function generateSVGPathsA() &#123;&#125;
function generateSVGPathsB() &#123;&#125;
function generateSVGTexts() &#123;&#125;
</pre><p><br></p><blockquote><em>Art is never finished, only abandoned.</em></blockquote><p>Logbook, though its contract code is static on the blockchain, when we write, transfer, fork, donate…every interaction makes it comes to life. We can co-create our story, in this untold digital space.</p>  
</div>
            