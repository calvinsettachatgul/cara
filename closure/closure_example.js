const addToCount = () => {
    
    let count = 0;
    
    const addOne = () => {
      console.log('before', {count});
      count++;
      console.log('after', {count});
    }
    return addOne;
    
};

const myCounter = addToCount();

myCounter();
myCounter();
myCounter();
