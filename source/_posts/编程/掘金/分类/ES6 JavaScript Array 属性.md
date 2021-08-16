
---
title: 'ES6 JavaScript Array 属性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f7bce12b70d409ea4bc18295b61e08a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 00:43:20 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f7bce12b70d409ea4bc18295b61e08a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:18px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:40px;margin-bottom:20px;color:#007fff;display:flex;align-items:center&#125;.markdown-body h1:hover:before,.markdown-body h2:hover:before,.markdown-body h3:hover:before,.markdown-body h4:hover:before,.markdown-body h5:hover:before,.markdown-body h6:hover:before&#123;transition:All .4s ease-in-out;transform:rotate(1turn)&#125;.markdown-body h1&#123;font-size:30px;background:linear-gradient(#fff 60%,#c6e3ff 0)&#125;.markdown-body h1:before&#123;content:"";display:inline-block;width:32px;height:32px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h2&#123;font-size:24px;background:linear-gradient(#fff 60%,#cce3fb 0)&#125;.markdown-body h2:before&#123;content:"";display:inline-block;width:24px;height:24px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3:before&#123;content:"";display:inline-block;width:18px;height:18px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h4&#123;font-size:18px&#125;.markdown-body h4:before&#123;content:"";display:inline-block;width:16px;height:16px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h5:before&#123;content:"";display:inline-block;width:15px;height:15px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h6&#123;font-size:14px&#125;.markdown-body h6:before&#123;content:"";display:inline-block;width:12px;height:12px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;border-bottom:2px solid #007fff;color:#007fff;padding-right:10px&#125;.markdown-body p&#123;letter-spacing:1px;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;display:block;max-width:100%;margin:10px auto&#125;.markdown-body hr&#123;border:none;border-top:1px dashed #92c8ff&#125;.markdown-body hr:before&#123;content:"✂";display:inline-block;position:relative;top:-12px;left:40px;padding:0 3px;color:#007fff;font-size:18px&#125;.markdown-body hr:after&#123;content:"按虚线剪开";position:relative;top:-15px;left:84%;padding:0 3px;color:#007fff;font-size:12px&#125;.markdown-body del&#123;color:#f44&#125;.markdown-body em&#123;color:#007fff;margin:0 2px&#125;.markdown-body strong&#123;color:#007fff;font-weight:bolder&#125;.markdown-body code&#123;word-break:break-word;border-radius:4px;overflow-x:auto;background-color:#e6f3ff;color:#007fff;font-weight:600;font-size:16px;padding:.065em .4em;border:1px solid #007fff&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:5px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:18px;font-weight:400;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8;border:none&#125;.markdown-body a&#123;text-decoration:none;color:#007fff;border-bottom:1px solid #007fff&#125;.markdown-body a:before&#123;content:"¶";margin-right:5px;font-size:22px&#125;.markdown-body a:after&#123;content:"↷";margin-left:2px;font-size:22px;display:none&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c;border-bottom:1px solid #275b8c&#125;.markdown-body a:active:after,.markdown-body a:hover:after&#123;display:inline-block&#125;.markdown-body table&#123;display:inline-block!important;font-size:16px;width:auto;max-width:100%;overflow:auto;border:1px solid #a5d3ff&#125;.markdown-body thead&#123;background:#c6e3ff;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#eef7ff&#125;.markdown-body tbody>tr:nth-child(odd)&#123;background-color:#f8fcff&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #007fff;background-color:#eef7ff&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#007fff&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f7bce12b70d409ea4bc18295b61e08a~tplv-k3u1fbpfcp-watermark.image" alt="bVcTZJu.webp" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">前言</h3>
<p>没有前言，直接开始，哈哈哈哈哈哈....</p>
<h2 data-id="heading-1">遍历数组方法</h2>
<h4 data-id="heading-2">forEach()</h4>
<p><code>forEach()</code> 方法按照升序为数组中每一项执行一次给定的函数。<br>
<strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.forEach(callback(currentValue , index , array) ，thisArg)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>currentValue</code> : 数组当前项值</li>
<li><code>index</code> : 数组当前项索引</li>
<li><code>arr</code> : 数组对象本身</li>
<li><code>thisArg</code> : 可选参数。当执行回调函数 <code>callback</code> 时，用作 <code>this</code> 的值。</li>
</ul>
<p><strong>注意</strong></p>
<ul>
<li>如果使用 <strong>箭头函数表达式</strong>来传入函数参数， <code>thisArg</code> 参数会被忽略，因为箭头函数在词法上绑定了 <code>this</code> 值。</li>
<li><code>forEach</code> 不会直接改变调用它的对象，但是那个对象可能会被 <code>callback</code> 函数改变。</li>
<li><code>every</code> 不会改变原数组。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">1</span>,<span class="hljs-number">44</span>]

arr.forEach(<span class="hljs-function"><span class="hljs-params">val</span> =></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`值为<span class="hljs-subst">$&#123;val*<span class="hljs-number">2</span>&#125;</span>`</span>)
    
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`原数组为<span class="hljs-subst">$&#123;arr&#125;</span>`</span>);
<span class="hljs-comment">// 值为4</span>
<span class="hljs-comment">// 值为6</span>
<span class="hljs-comment">// 值为8</span>
<span class="hljs-comment">// 值为2</span>
<span class="hljs-comment">// 值为88</span>
<span class="hljs-comment">// 原数组为2,3,4,1,44</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">reduce()</h4>
<p><code>reduce()</code>数组元素累计器，返回一个合并的结果值。
<strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.reduce(callback(accumulator, currentValue, index, array), initialValue)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>accumulator</code> : 累计器，默认为数组元素第一个值</li>
<li><code>currentValue</code> : 当前值</li>
<li><code>index</code> : 当前元素索可选</li>
<li><code>array</code> : 数组可选</li>
<li><code>initialValue</code> : 初始值可选</li>
</ul>
<p><code>reduce</code> 有两个参数，一个是回调函数，一个是初始值。
它有两种取值情况：</p>
<ol>
<li>当提供了 <code>initialValue</code> 初始值时， 那么<code>accumulator</code> 的值为 <code>initialValue</code> , <code>currentValue</code> 的值为 数组第一个值</li>
<li>当没有提供 <code>initialValue</code> 初始值时， 那么 <code>accumulator</code> 的值 为 数组第一个值， <code>currentValue</code> 为第二个值。</li>
</ol>
<p><strong>注意</strong></p>
<ul>
<li>如果数组为空，且没有提供<code>initialValue</code> 初始值时，会抛出 <code>TypeError</code> .</li>
<li>如果数组有一个元素，且没有提供<code>initialValue</code> 或者 提供了<code>initialValue</code> ，数组为空，那么唯一值被返回不会执行 <code>callback</code> 回调函数。</li>
</ul>
<p><strong>求和</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]

<span class="hljs-keyword">const</span> sum = arr.reduce(<span class="hljs-function">(<span class="hljs-params">accumulator, currentValue</span>) =></span> accumulator + currentValue, <span class="hljs-number">10</span>)

<span class="hljs-built_in">console</span>.log(sum) <span class="hljs-comment">//20 </span>
<span class="hljs-comment">// accumulator  累计器</span>
<span class="hljs-comment">// currentValue  当前值</span>
<span class="hljs-comment">// initialValue  累计 初始值 为10 </span>

<span class="hljs-comment">//10 + 1 + 2 + 3 + 4</span>


<span class="hljs-comment">//## 注意</span>
<span class="hljs-comment">// 回调函数第一次执行时，accumulator 和currentValue的取值有两种情况：</span>
<span class="hljs-comment">// 如果调用reduce()时提供了initialValue，accumulator取值为initialValue，currentValue取数组中的第一个值；</span>
<span class="hljs-comment">// 如果没有提供 initialValue，那么accumulator取数组中的第一个值，currentValue取数组中的第二个值。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>计算对象中的值</strong><br>
要累加对象数组中包含的值，必须提供初始值，以便各个item正确通过你的函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> data = [
    &#123;
        <span class="hljs-attr">date</span>: <span class="hljs-string">'2021-8-1'</span>,
        <span class="hljs-attr">income</span>: <span class="hljs-number">200</span>
    &#125;,
    &#123;
        <span class="hljs-attr">date</span>: <span class="hljs-string">'2021-8-2'</span>,
        <span class="hljs-attr">income</span>: <span class="hljs-number">400</span>
    &#125;,
    &#123;
        <span class="hljs-attr">date</span>: <span class="hljs-string">'2021-8-3'</span>,
        <span class="hljs-attr">income</span>: <span class="hljs-number">300</span>
    &#125;,
]

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`总收入： <span class="hljs-subst">$&#123;data.reduce( (pre,currentValue) => pre + currentValue.income,<span class="hljs-number">0</span>)&#125;</span>`</span>);
<span class="hljs-comment">//总收入： 900</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>二维数组转一位数组</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> array = [[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>],[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]]
<span class="hljs-built_in">console</span>.log(array.reduce(<span class="hljs-function">(<span class="hljs-params">a,b</span>) =></span> a.concat(b)));
<span class="hljs-comment">//[ 1, 2, 3, 4 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">find()</h4>
<p><code>find()</code> 返回满足特定条件的元素对象或者元素值， 不满足返回 <code>undefined</code>语法</p>
<pre><code class="hljs language-js copyable" lang="js">arr.find((element,index,array), thisArg)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>element</code> ： 当前元素</li>
<li><code>index</code> : 当前元素索引可选</li>
<li><code>array</code> : 数组本身可选</li>
<li><code>thisArg</code> : 执行回调时用作<code>this</code> 的对象可选</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 从数据中找出第一个满足特定条件的对象</span>
<span class="hljs-keyword">const</span> data = [
    &#123;
        <span class="hljs-attr">name</span>:<span class="hljs-string">'张三'</span>,
        <span class="hljs-attr">article</span>: <span class="hljs-number">3</span>
    &#125;,
    &#123;
        <span class="hljs-attr">name</span>:<span class="hljs-string">'老王'</span>,
        <span class="hljs-attr">article</span>: <span class="hljs-number">9</span>
    &#125;,
    &#123;
        <span class="hljs-attr">name</span>:<span class="hljs-string">'老李'</span>,
        <span class="hljs-attr">article</span>: <span class="hljs-number">10</span>
    &#125;
]

<span class="hljs-built_in">console</span>.log(data.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.article > <span class="hljs-number">9</span> ));

<span class="hljs-comment">// &#123; name: '老李', article: 10 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">findIndex()</h4>
<p><code>findIndex()</code> 返回数组中符合条件的第一个元素的索引，没有，则返回 <code>-1</code> 。<br>
<strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.findIndex((element,index,array), thisArg)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>element</code> ： 当前元素</li>
<li><code>index</code> : 当前元素索引可选</li>
<li><code>array</code> : 数组本身可选</li>
<li><code>thisArg</code> : 执行回调时用作<code>this</code> 的对象可选</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">22</span>,<span class="hljs-number">33</span>,<span class="hljs-number">44</span>,<span class="hljs-number">55</span>]
<span class="hljs-built_in">console</span>.log(arr.findIndex(<span class="hljs-function"><span class="hljs-params">val</span> =></span> val > <span class="hljs-number">33</span>));    <span class="hljs-comment">//2</span>
<span class="hljs-built_in">console</span>.log(arr.findIndex(<span class="hljs-function"><span class="hljs-params">val</span> =></span> val > <span class="hljs-number">99</span>));    <span class="hljs-comment">//-1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">key()</h4>
<p><code>key()</code> 返回一个新的<strong>Array Iterator</strong>对象，该对象包含数组中每个索引的键。</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">keys()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong></p>
<ul>
<li>如果数组中有空原元素，在获取key 时， 也会加入遍历的队列中。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> inputModal = [
    &#123;
        <span class="hljs-attr">name</span>:<span class="hljs-string">''</span>
    &#125;,
    &#123;
        <span class="hljs-attr">age</span>:<span class="hljs-string">''</span>
    &#125;,
    &#123;
        <span class="hljs-attr">hobby</span>:<span class="hljs-string">''</span>
    &#125;
]
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> key <span class="hljs-keyword">of</span> inputModal.keys())&#123;
    <span class="hljs-built_in">console</span>.log(key)
&#125;
<span class="hljs-comment">// 0</span>
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>

<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,,<span class="hljs-number">3</span>]
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> key <span class="hljs-keyword">of</span> arr.keys())&#123;
    <span class="hljs-built_in">console</span>.log(key);
&#125;
<span class="hljs-comment">// 0</span>
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 2</span>
<span class="hljs-comment">// 3</span>


<span class="hljs-comment">//Object.keys() 方法会返回一个由一个给定对象的自身可枚举属性组成的数组</span>
<span class="hljs-comment">// 所以 Object.keys(arr) = [ '0', '1', '3' ]</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> key <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.keys(arr))&#123;
    <span class="hljs-built_in">console</span>.log(key);
&#125;
<span class="hljs-comment">// 0</span>
<span class="hljs-comment">// 1</span>
<span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">values()</h4>
<p><code>values() </code>方法返回一个新的 <strong>Array Iterator</strong> 对象，该对象包含数组每个索引的值。</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.values()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Color = [<span class="hljs-string">'red'</span>,<span class="hljs-string">'yelloe'</span>,<span class="hljs-string">'orange'</span>]

<span class="hljs-keyword">for</span>(val <span class="hljs-keyword">of</span> Color.values())&#123;
    <span class="hljs-built_in">console</span>.log(val);
&#125;
<span class="hljs-comment">// red</span>
<span class="hljs-comment">// yelloe</span>
<span class="hljs-comment">// orange</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">返回 布尔值</h3>
<h4 data-id="heading-9">every()</h4>
<p><code>every</code> 用来判断数组内所有元素是否符合某个条件，返回 <strong>布尔值</strong>
<strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.every(callback(currentValue , index , array) ，thisArg)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>currentValue</code> : 数组当前项值必须</li>
<li><code>index</code> : 数组当前项索引可选</li>
<li><code>arr</code> : 数组对象本身可选</li>
<li><code>thisArg</code> : 可选参数。当执行回调函数 <code>callback</code> 时，用作 <code>this</code> 的值可选</li>
</ul>
<p><strong>注意</strong></p>
<ul>
<li>当所有的元素都符合条件才会返回<code>true</code></li>
<li><code>every</code> 不会改变原数组。</li>
<li>若传入一个空数组，无论如何都会返回 <code>true</code>。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">1</span>,<span class="hljs-number">44</span>]

<span class="hljs-built_in">console</span>.log(arr.every(<span class="hljs-function"><span class="hljs-params">val</span> =></span>  val > <span class="hljs-number">0</span> ));   <span class="hljs-comment">//true</span>

<span class="hljs-built_in">console</span>.log(arr.every(<span class="hljs-function"><span class="hljs-params">val</span> =></span> &#123; val > <span class="hljs-number">2</span> &#125;)) <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">some()</h4>
<p><code>some()</code> 用来判断数组元素是否符合某个条件，只要有一个元素符合，那么返回 <code>true</code>.</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.some(callback(currentValue , index , array) ，thisArg)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>currentValue</code> : 数组当前项值必须</li>
<li><code>index</code> : 数组当前项索引可选</li>
<li><code>arr</code> : 数组对象本身可选</li>
<li><code>thisArg</code> : 可选参数。当执行回调函数 <code>callback</code> 时，用作 <code>this</code> 的值可选</li>
</ul>
<p><strong>注意</strong></p>
<ul>
<li><code>some()</code> 被调用时不会改变数组。</li>
<li>如果用一个空数组进行测试，在任何情况下它返回的都是<code>false</code>。</li>
<li><code>some()</code> 在遍历时，元素范围已经确定，在遍历过程中添加的元素，不会加入到遍历的序列中。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">1</span>,<span class="hljs-number">44</span>]

<span class="hljs-built_in">console</span>.log(arr.some(<span class="hljs-function"><span class="hljs-params">val</span> =></span> val > <span class="hljs-number">2</span>))  <span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log([].some(<span class="hljs-function"><span class="hljs-params">val</span> =></span> val > <span class="hljs-number">2</span> )); <span class="hljs-comment">//false</span>

<span class="hljs-keyword">const</span> newList = [<span class="hljs-number">11</span>,<span class="hljs-number">22</span>,<span class="hljs-number">33</span>,<span class="hljs-number">44</span>]
<span class="hljs-built_in">console</span>.log(newList.some(<span class="hljs-function"><span class="hljs-params">val</span> =></span> &#123;
    newList.push(<span class="hljs-number">55</span>)
    newList.push(<span class="hljs-number">66</span>)
    val > <span class="hljs-number">55</span>
&#125;));   <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">不改变原有数组，形成新的数组</h3>
<h4 data-id="heading-12">filter()</h4>
<p><code>filter()</code> 用来遍历原数组，过滤拿到符合条件的数组元素，形成新的数组元素。
<strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.some(callback(currentValue , index , array) ，thisArg)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>currentValue</code> : 数组当前项值必须</li>
<li><code>index</code> : 数组当前项索引可选</li>
<li><code>arr</code> : 数组对象本身可选</li>
<li><code>thisArg</code> : 可选参数。当执行回调函数 <code>callback</code> 时，用作 <code>this</code> 的值可选</li>
</ul>
<p><strong>注意</strong></p>
<ul>
<li><code>filter</code> 不会改变原数组，它返回过滤后的新数组。</li>
<li><code>filter()</code> 在遍历时，元素范围已经确定，在遍历过程中添加的元素，不会加入到遍历的序列中。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">11</span>,<span class="hljs-number">22</span>,<span class="hljs-number">33</span>,<span class="hljs-number">44</span>,<span class="hljs-number">55</span>,<span class="hljs-number">66</span>]
<span class="hljs-built_in">console</span>.log(arr.filter(<span class="hljs-function"><span class="hljs-params">val</span> =></span> val > <span class="hljs-number">44</span> ))
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">`原数组为<span class="hljs-subst">$&#123;arr&#125;</span>`</span>);

<span class="hljs-comment">// [ 55, 66 ]</span>
<span class="hljs-comment">// 原数组为11,22,33,44,55,66</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">map()</h4>
<p><code>map()</code> 创建一个新的数组，其结果是该数组中的每个元素都调用一个提供的函数后返回的结果。</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.map(callback(currentValue , index , array) ，thisArg)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>currentValue</code> : 数组当前项值必须</li>
<li><code>index</code> : 数组当前项索引可选</li>
<li><code>arr</code> : 数组对象本身可选</li>
<li><code>thisArg</code> : 可选参数。当执行回调函数 <code>callback</code> 时，用作 <code>this</code> 的值可选</li>
</ul>
<p><strong>注意</strong></p>
<ul>
<li><code>map </code>不修改调用它的原数组本身</li>
<li><code>map()</code> 在遍历时，元素范围已经确定，在遍历过程中添加的元素，不会加入到遍历的序列中。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]
<span class="hljs-built_in">console</span>.log(arr.map(<span class="hljs-function"><span class="hljs-params">val</span> =></span> val*<span class="hljs-number">3</span> ))  <span class="hljs-comment">// [ 3, 6, 9, 12 ]</span>
<span class="hljs-built_in">console</span>.log(arr)  <span class="hljs-comment">// [ 1, 2, 3, 4 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">数组 CRUD</h2>
<h3 data-id="heading-15">改变原数组方法</h3>
<h4 data-id="heading-16">reverse()</h4>
<p><code>reverse()</code> 方法将数组中元素的位置颠倒，并返回该数组。数组的第一个元素会变成最后一个，数组的最后一个元素变成第一个。该方法会改变原数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]

<span class="hljs-built_in">console</span>.log(arr.reverse(<span class="hljs-number">11</span>,<span class="hljs-number">22</span>,<span class="hljs-number">33</span>))  <span class="hljs-comment">//[ 3, 2, 1 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">sort()</h4>
<p><code>sort()</code> 方法采用 <strong>原地算法</strong>进行排序并返回数组。默认排序顺序是在<strong>将元素转换为字符串</strong>，然后<strong>比较它们的<code>UTF-16</code>代码单元值序列</strong></p>
<p><strong>原地算法</strong>是一个使用辅助的数据结构对输入进行转换的算法。但是，它允许有少量额外的存储空间来储存辅助变量。当算法运行时，输入通常会被输出覆盖。原地算法仅通过替换或交换元素来更新输入序列。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">23</span>,<span class="hljs-number">11</span>,<span class="hljs-number">33</span>,<span class="hljs-number">44</span>,<span class="hljs-number">1</span>]

<span class="hljs-built_in">console</span>.log(arr.sort())  <span class="hljs-comment">//[ 1, 11, 23, 33, 44 ]</span>


<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">23</span>,<span class="hljs-number">11</span>,<span class="hljs-number">33</span>,<span class="hljs-number">44</span>,<span class="hljs-number">1000000000</span>]

<span class="hljs-built_in">console</span>.log(arr.sort())  
<span class="hljs-comment">// [ 1000000000, 11, 23, 33, 44 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">删除元素</h3>
<h4 data-id="heading-19">shift()</h4>
<p><code>shift()</code> 方法从数组中删除<strong>第一个</strong>元素，并返回该元素的值。此方法更改数组的长度。</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.shift()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong></p>
<ul>
<li>从数组中删除的元素; 如果数组为空则返回<code>undefined</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> data = [
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">1</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'前端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">2</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'后端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">3</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'移动端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">4</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'嵌入式开发'</span>
    &#125;,
]

<span class="hljs-keyword">const</span> deleObj = data.shift()



<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'==============删除后的元素======================'</span>);
<span class="hljs-built_in">console</span>.log(data);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'=================删除后的元素==================='</span>);


<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'===============被删除的元素====================='</span>);
<span class="hljs-built_in">console</span>.log(deleObj);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'================被删除的元素===================='</span>);

<span class="hljs-comment">//  ==============删除后的元素======================</span>
<span class="hljs-comment">// [</span>
<span class="hljs-comment">//     &#123; id: 2, name: '后端' &#125;,</span>
<span class="hljs-comment">//     &#123; id: 3, name: '移动端' &#125;,</span>
<span class="hljs-comment">//     &#123; id: 4, name: '嵌入式开发' &#125;</span>
<span class="hljs-comment">//   ]</span>
<span class="hljs-comment">//   =================删除后的元素===================</span>

  
<span class="hljs-comment">//   ===============被删除的元素=====================</span>
<span class="hljs-comment">//   &#123; id: 1, name: '前端' &#125;</span>
<span class="hljs-comment">//   ================被删除的元素====================</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">pop()</h4>
<p><code>pop()</code>方法从数组中删除最后一个元素，并返回该元素的值。此方法更改数组的长度。</p>
<p>用法和 <code>shift</code> 类似。</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.pop()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong></p>
<ul>
<li>从数组中删除的元素; 如果数组为空则返回<code>undefined</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> data = [
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">1</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'前端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">2</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'后端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">3</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'移动端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">4</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'嵌入式开发'</span>
    &#125;,
]

<span class="hljs-keyword">const</span> deleObj = data.pop()




<span class="hljs-built_in">console</span>.log(data);
<span class="hljs-comment">// [</span>
<span class="hljs-comment">//     &#123; id: 1, name: '前端' &#125;,</span>
<span class="hljs-comment">//     &#123; id: 2, name: '后端' &#125;,</span>
<span class="hljs-comment">//     &#123; id: 3, name: '移动端' &#125;</span>
<span class="hljs-comment">// ]</span>
<span class="hljs-built_in">console</span>.log(deleObj);
<span class="hljs-comment">// &#123; id: 4, name: '嵌入式开发' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">splice()</h4>
<p><code>splice()</code> 方法通过<strong>删除</strong>或<strong>替换</strong>现有元素或者原地添加新的元素来修改数组,并以数组形式返回被修改的内容。此方法会改变原数组。</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">array.splice(start,deleteCount, [item1,item2....])
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>start</code> : 开始的索引</li>
<li><code>deleteCount</code> : 删除的个数 可选</li>
<li><code>[item1，item2 .....]</code> ；从开始的索引进行 添加的增加和替换的元素， 可选</li>
</ul>
<p><strong>注意</strong></p>
<ul>
<li>由被删除的元素组成的一个数组。如果只删除了一个元素，则返回只包含一个元素的数组。如果没有删除元素，则返回空数组。</li>
<li>如果只传递了开始的索引位置，则会删除索引后的所有元素对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> data = [
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">1</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'前端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">2</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'后端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">3</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'移动端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">4</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'嵌入式开发'</span>
    &#125;,
]
data.splice(<span class="hljs-number">1</span>)
<span class="hljs-built_in">console</span>.log(data)
<span class="hljs-comment">// [ &#123; id: 1, name: '前端' &#125; ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>从索引为 2 开始， 删除 1 个数组元素对象，添加两个数组元素对象</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> data = [
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">1</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'前端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">2</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'后端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">3</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'移动端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">4</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'嵌入式开发'</span>
    &#125;,
]


data.splice(<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,...[&#123;<span class="hljs-attr">id</span>:<span class="hljs-number">5</span>,<span class="hljs-attr">name</span>:<span class="hljs-string">'人工智能'</span>&#125;,&#123;<span class="hljs-attr">id</span>:<span class="hljs-number">6</span>,<span class="hljs-attr">name</span>:<span class="hljs-string">'大数据开发'</span>&#125;])

<span class="hljs-built_in">console</span>.log(data);
<span class="hljs-comment">// [</span>
<span class="hljs-comment">//     &#123; id: 1, name: '前端' &#125;,</span>
<span class="hljs-comment">//     &#123; id: 2, name: '后端' &#125;,</span>
<span class="hljs-comment">//     &#123; id: 5, name: '人工智能' &#125;,</span>
<span class="hljs-comment">//     &#123; id: 6, name: '大数据开发' &#125;,</span>
<span class="hljs-comment">//     &#123; id: 4, name: '嵌入式开发' &#125;</span>
<span class="hljs-comment">// ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">增加元素</h3>
<h4 data-id="heading-23">splice()</h4>
<p>上面已经有介绍</p>
<h4 data-id="heading-24">push()</h4>
<p><code>push()</code> 方法将一个或多个元素添加到数组的<strong>末尾</strong>，并返回该数组的新长度。</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.push(element1, ..., elementN)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> data = [
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">1</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'前端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">2</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'后端'</span>
    &#125;,
]

<span class="hljs-built_in">console</span>.log(data.push(&#123;<span class="hljs-attr">id</span>:<span class="hljs-number">3</span>,<span class="hljs-attr">name</span>:<span class="hljs-string">'移动端'</span>&#125;))  <span class="hljs-comment">//3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>合并数组</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> data = [
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">1</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'前端'</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">2</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'后端'</span>
    &#125;,
]


<span class="hljs-keyword">var</span> obj = [
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">4</span>,
        <span class="hljs-attr">name</span>:<span class="hljs-string">'嵌入式开发'</span>
    &#125;,
]

<span class="hljs-comment">// 相当于 data.push(&#123;id:4,name:'嵌入式开发'&#125;);</span>
<span class="hljs-built_in">Array</span>.prototype.push.apply(data, obj);

<span class="hljs-built_in">console</span>.log(data);

[
  &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'前端'</span> &#125;,
  &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'后端'</span> &#125;,
  &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">4</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'嵌入式开发'</span> &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">unshift()</h4>
<p><code>unshift()</code> 方法将一个或多个元素添加到数组的<strong>开头</strong>，并返回该数组的<strong>新长度</strong>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]

<span class="hljs-built_in">console</span>.log(arr.unshift(<span class="hljs-number">11</span>,<span class="hljs-number">22</span>,<span class="hljs-number">33</span>))  <span class="hljs-comment">//6 </span>
<span class="hljs-built_in">console</span>.log(arr)  <span class="hljs-comment">//[ 11, 22, 33, 1, 2, 3 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">不改变原数组元素方法</h3>
<h4 data-id="heading-27">indexOf()</h4>
<p><code>indexOf()</code>方法返回可以在数组中找到给定元素的第一个索引，如果不存在，则返回 -1。</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">indexOf(searchElement)
indexOf(searchElement, fromIndex)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><code>searchElement</code> : 要查找的元素</p>
</li>
<li>
<p><code>fromIndex</code> ： 按指定的索引进行查找出现的指定元素的第一个索引可选</p>
<ul>
<li>如果索引大于或等于数组的长度，则返回-1</li>
<li>如果提供的索引值为负数，则将其视为距数组末尾的偏移量</li>
<li>如果提供的索引为负数，仍然从前到后搜索数组</li>
<li>如果提供的索引为 0，则将搜索整个数组。</li>
<li>默认值：0（搜索整个数组）。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">4</span>,<span class="hljs-number">4</span>,<span class="hljs-number">6</span>]

<span class="hljs-built_in">console</span>.log(arr.indexOf(<span class="hljs-number">3</span>));  <span class="hljs-comment">//3</span>
<span class="hljs-built_in">console</span>.log(arr.indexOf(<span class="hljs-number">9</span>));  <span class="hljs-comment">//-1</span>

<span class="hljs-built_in">console</span>.log(arr.indexOf(<span class="hljs-number">3</span>,<span class="hljs-number">4</span>)); <span class="hljs-comment">//-1</span>
<span class="hljs-comment">//从索引为 4 的元素进行查找 3, 显然后面没有3 ， 返回 -1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>数组去重</strong></p>
<p>创建一个新的空数组，通过<code>indexOf</code> 来判断空数组是否第一次存在某个元素，</p>
<ul>
<li>不存在则返回 [ < 0 ] ，<code>push</code> 到空数组中.</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> newArr = []
arr.forEach(<span class="hljs-function"><span class="hljs-params">val</span> =></span> &#123;
    <span class="hljs-keyword">if</span>(newArr.indexOf(val) < <span class="hljs-number">0</span>)&#123;
       newArr.push(val)
    &#125;
&#125;)
<span class="hljs-built_in">console</span>.log(newArr);
<span class="hljs-comment">// [ 1, 2, 3, 4, 5, 6 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">lastIndexOf()</h4>
<p><code>lastIndexOf()</code> 查找数组中元素最后一次出现的索引，如未找到返回-1。</p>
<p>如果不存在则返回 -1。从数组的后面向前查找，从 <code>fromIndex</code> 处开始。</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.lastIndexOf(searchElement, fromIndex)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><code>searchElement</code> : 要查找的元素</p>
</li>
<li>
<p><code>fromIndex</code> ： 按指定的索引进行查找出现的指定元素的第一个索引。 可选</p>
<ul>
<li>从指定的索引位置 <strong>逆向</strong> 查找</li>
<li>默认为数组的长度减 <code>1(arr.length - 1</code>)，即整个数组都被查找。</li>
<li>如果该值大于或等于数组的长度，则整个数组会被查找。</li>
<li>如果为负值，数组仍然会被从后向前查找。</li>
<li>如果该值为负时，其绝对值大于数组长度，则方法返回 -1，即数组不会被查找。</li>
</ul>
</li>
</ul>
<p><strong>注意</strong></p>
<ul>
<li><code>lastIndexOf</code> 使用的是 <strong>严格相等</strong> === 比较 <code>searchElement</code> 和数组中的元素。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">4</span>,<span class="hljs-number">4</span>,<span class="hljs-number">6</span>]

<span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">4</span>)); <span class="hljs-comment">//7</span>

<span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">4</span>,<span class="hljs-number">11</span>));  
<span class="hljs-comment">//7    指定的查找的索引 大于 数组的长度， 会进行整个数组查找</span>

<span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">4</span>,-<span class="hljs-number">33</span>));
<span class="hljs-comment">// -1   指定的索引为负数，且绝对值大于数组长度， 则返回 -1</span>

<span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">4</span>,-<span class="hljs-number">5</span>));
<span class="hljs-comment">//4    指定的索引为负数，且绝对值小于数组长度， 则会 从向前进行查找</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29"><code>inCludes()</code></h4>
<p><code>includes()</code> 方法用来判断一个数组是否包含一个指定的值，根据情况，如果包含则返回 true，否则返回false。</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.includes(searchElement, fromIndex)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><code>searchElement</code> : 要查找的元素</p>
<blockquote>
<p>查找时，区分大小写</p>
</blockquote>
</li>
<li>
<p><code>fromIndex</code> ： 按指定的索引进行查找出现的指定元素的第一个索引。 可选</p>
<ul>
<li>从指定的索引进行查找</li>
<li>如果为负值，则按升序从 <code>array.length + fromIndex</code> 的索引开始搜</li>
<li>如果 <code>fromIndex</code> 大于等于数组的长度，则会返回 <code>false</code>，且该数组不会被搜索。</li>
<li>默认为0</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">4</span>,<span class="hljs-number">4</span>,<span class="hljs-number">6</span>]

<span class="hljs-built_in">console</span>.log(arr.includes(<span class="hljs-number">4</span>)); <span class="hljs-comment">//true</span>

<span class="hljs-built_in">console</span>.log(arr.includes(<span class="hljs-number">4</span>,<span class="hljs-number">66</span>)); <span class="hljs-comment">//false</span>

<span class="hljs-built_in">console</span>.log(arr.includes(<span class="hljs-number">1</span>,-<span class="hljs-number">1</span>)); <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">concat()</h4>
<p><code>concat()</code> 方法用于合并两个或多个数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> new_array = old_array.concat([arr1][arr2])
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong></p>
<ul>
<li>
<p><code>concat</code>方法不会改变<code>this</code>或任何作为参数提供的数组，而是返回一个<strong>浅拷贝</strong>，它包含与原始数组相结合的相同元素的副本</p>
<ul>
<li>对象引用（而不是实际对象）：<code>concat</code>将对象引用复制到新数组中。 原始数组和新数组都引用相同的对象。 也就是说，如果引用的对象被修改，则更改对于新数组和原始数组都是可见的。 这包括也是数组的数组参数的元素。</li>
<li>数据类型如字符串，数字和布尔（不是<code>String</code>，<code>Number</code>和 <code>Boolean</code>) 对象）：<code>concat</code>将字符串和数字的值复制到新数组中。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr1 = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]
<span class="hljs-keyword">let</span> arr2 = [<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]
<span class="hljs-keyword">let</span> arr3 = [[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>],[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]]
<span class="hljs-built_in">console</span>.log(arr1.concat(arr2));
<span class="hljs-comment">//[ 1, 2, 3, 4, 5, 6 ]</span>

<span class="hljs-comment">// 嵌套合并</span>
<span class="hljs-built_in">console</span>.log(arr1.concat(arr2).concat(arr3));
<span class="hljs-comment">// [ 1, 2, 3, 4, 5, 6, [ 1, 2 ], [ 3, 4 ] ]</span>


<span class="hljs-keyword">let</span> obj1 = [&#123;<span class="hljs-attr">a</span>:<span class="hljs-number">1</span>&#125;,&#123;<span class="hljs-attr">b</span>:<span class="hljs-number">2</span>&#125;]
<span class="hljs-keyword">let</span> obj2 = [&#123;<span class="hljs-attr">c</span>:<span class="hljs-number">3</span>&#125;,&#123;<span class="hljs-attr">d</span>:<span class="hljs-number">4</span>&#125;]
<span class="hljs-keyword">let</span> obj3 = obj1.concat(obj2)  
<span class="hljs-built_in">console</span>.log(obj3); 
<span class="hljs-comment">//[ &#123; a: 1 &#125;, &#123; b: 2 &#125;, &#123; c: 3 &#125;, &#123; d: 4 &#125; ]</span>


obj1[<span class="hljs-number">0</span>].a = <span class="hljs-number">4</span>  <span class="hljs-comment">//改变obj[0]对象值，会直接影响合并后的数组，因为是浅拷贝</span>
<span class="hljs-built_in">console</span>.log(obj3); 
<span class="hljs-comment">//[ &#123; a: 4 &#125;, &#123; b: 2 &#125;, &#123; c: 3 &#125;, &#123; d: 4 &#125; ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">toString()</h4>
<p><code>toString()</code> 返回一个字符串，表示指定的数组及其元素。</p>
<p><strong>当一个数组被作为文本值或者进行字符串连接操作时，将会自动调用其 <code>toString</code> 方法。</strong></p>
<p>对于数组对象，<code>toString</code> 方法连接数组并返回一个字符串，其中包含用逗号分隔的每个数组元素。</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.toString()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]

<span class="hljs-built_in">console</span>.log(arr.toString());  <span class="hljs-comment">//1,2,3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">join()</h4>
<p><code>join()</code>方法通过连接数组元素用逗号或指定的分隔符字符串分隔，返回一个字符串。</p>
<p>如果数组只有一项，则将在不使用分隔符的情况下返回该项。</p>
<p><strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">join()
join(separator)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>separator</code> : 指定的分割的字符可选</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-string">'2021'</span>,<span class="hljs-string">'08'</span>,<span class="hljs-string">'08'</span>]

<span class="hljs-built_in">console</span>.log(arr.join());     <span class="hljs-comment">//2021,08,08</span>
<span class="hljs-built_in">console</span>.log(arr.join(<span class="hljs-string">'-'</span>));  <span class="hljs-comment">//2021-08-08</span>
<span class="hljs-built_in">console</span>.log(arr.join(<span class="hljs-string">'/'</span>));  <span class="hljs-comment">//2021/08/08</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">slice()</h4>
<p><code>slice()</code> 方法返回一个新的数组对象，这一对象是一个由 <code>begin</code> 和 <code>end</code> 决定的原数组的<strong>浅拷贝</strong>（包括 <code>begin</code>，不包括<code>end</code>）。原始数组不会被改变。
<strong>语法</strong></p>
<pre><code class="hljs language-js copyable" lang="js">arr.slice(begin, end)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><code>begin</code> : 指定截取的<strong>开始</strong>索引 可选</p>
<ul>
<li>默认从0 开始</li>
<li>如果<code>begin</code> 为负数，则以数组末尾开始 的 绝对值开始截取 <code>slice(-2)</code> 末尾第2个元素</li>
<li>如果 <code>begin</code> 超出原数组的索引范围，则会返回空数组。</li>
</ul>
</li>
<li>
<p><code>end</code> : 指定截取的<strong>结束</strong>索引 可选</p>
<ul>
<li>如果 <code>end</code> 被省略，则 <code>slice</code> 会一直提取到原数组末尾。</li>
<li>如果 <code>end</code> 大于数组的长度，<code>slice</code> 也会一直提取到原数组末尾。</li>
<li>如果 <code>end</code> 为负数， 则它表示在原数组中的倒数第几个元素结束抽取。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">11</span>,<span class="hljs-number">22</span>,<span class="hljs-number">33</span>,<span class="hljs-number">44</span>,<span class="hljs-number">55</span>,<span class="hljs-number">66</span>,<span class="hljs-number">77</span>,<span class="hljs-number">88</span>]
<span class="hljs-built_in">console</span>.log(arr.slice(<span class="hljs-number">1</span>,<span class="hljs-number">4</span>));
<span class="hljs-comment">// 应该返回 索引 1 - 3 的数组元素</span>
<span class="hljs-comment">// [ 22, 33, 44 ]</span>

<span class="hljs-built_in">console</span>.log(arr.slice(-<span class="hljs-number">4</span>,<span class="hljs-number">2</span>))  <span class="hljs-comment">//[]</span>

<span class="hljs-built_in">console</span>.log(arr.slice(-<span class="hljs-number">4</span>));   <span class="hljs-comment">//[ 55, 66, 77, 88 ]</span>

<span class="hljs-built_in">console</span>.log(arr.slice(<span class="hljs-number">0</span>,-<span class="hljs-number">1</span>));
<span class="hljs-comment">// [</span>
<span class="hljs-comment">//     11, 22, 33, 44,</span>
<span class="hljs-comment">//     55, 66, 77</span>
<span class="hljs-comment">//   ]</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            