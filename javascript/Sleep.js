/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    // used to return promise 
  return  new Promise((resolve) => {
        setTimeout(resolve,  millis);
  });    

}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */